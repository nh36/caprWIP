-- paragraph_gloss_validator.lua
-- Validation-only Pandoc Lua filter:
-- Checks that the first lexical form in each prose paragraph (Part I only)
-- is followed by an immediate quoted gloss.
--
-- Scope:
--   Checks plain Markdown *italic* (Emph) and .iv-span forms.
--   Skips .pred spans (counterfactual forms) entirely.
--   Skips Part II "Word-by-word derivations" and later.
--
-- A "lexical form" is an italic form that passes is_lexical():
--   * at least 2 characters after trimming
--   * not an all-caps abbreviation ≤ 4 chars (OE, PGmc, ON, etc.)
--   * does not contain TeX/code metacharacters
--
-- The gloss check looks for the next non-space inline being:
--   * a Str starting with ' " ` \u2018 \u2019 \u201c \u201d, or
--   * a Quoted node.

local pandoc = require 'pandoc'
local utils = pandoc.utils

local failures = {}
local paragraphs_checked = 0
local first_occurrence_candidates = 0
local emph_occurrences = 0
local in_lexical_derivations = false

local function normalize(s)
  return (string.lower(s):gsub("[^%w]", ""))
end

local function is_lexical(form)
  local s = form:match("^%s*(.-)%s*$")
  if not s or #s < 2 then return false end
  -- All-caps abbreviation (OE, PGmc, ON, WS, etc.)
  if #s <= 4 and s:upper() == s then return false end
  -- TeX/code metacharacters leaking into prose
  if s:find("[\\{}|<>]") then return false end
  return true
end

local function span_has_class(span, class_name)
  if not span.classes then return false end
  for _, c in ipairs(span.classes) do
    if c == class_name then return true end
  end
  return false
end

-- Extract the italic text from a .iv span, if present.
local function form_from_iv_span(span)
  for _, child in ipairs(span.content) do
    if child.t == 'Emph' then
      return utils.stringify(child)
    end
  end
  return nil
end

-- Robust opening-quote test using raw byte values.
-- sub(1,1) returns only the first byte, so \u{...} comparisons fail for
-- multi-byte UTF-8.  Use byte arithmetic instead.
-- Recognised:
--   U+0027 straight apostrophe, U+0022 straight double, U+0060 backtick
--   U+2018 left single  (E2 80 98)
--   U+2019 right single (E2 80 99)  -- sometimes used as opening
--   U+201C left double  (E2 80 9C)
--   U+201D right double (E2 80 9D)  -- sometimes used as opening
local function starts_with_opening_quote(text)
  if not text or text == "" then return false end
  local b1 = text:byte(1)
  if b1 == 0x27 or b1 == 0x22 or b1 == 0x60 then return true end
  if b1 == 0xE2 and #text >= 3 then
    local b2 = text:byte(2)
    local b3 = text:byte(3)
    if b2 == 0x80
      and (b3 == 0x98 or b3 == 0x99 or b3 == 0x9C or b3 == 0x9D)
    then
      return true
    end
  end
  return false
end

local function has_gloss_after(content, idx)
  local j = idx + 1
  while j <= #content do
    local nxt = content[j]
    -- Skip Space and SoftBreak between form and gloss (SoftBreak occurs when
    -- a form sits at the end of a Markdown source line and its gloss begins
    -- the next line within the same paragraph).
    if nxt.t == 'Space' or nxt.t == 'SoftBreak' then
      j = j + 1
    elseif nxt.t == 'Str' then
      return starts_with_opening_quote(nxt.text)
    elseif nxt.t == 'Quoted' then
      return true
    else
      return false
    end
  end
  return false
end

function Header(el)
  local text = utils.stringify(el)
  if text == 'Word-by-word derivations' then
    in_lexical_derivations = true
  end
  return nil
end

function Para(el)
  if in_lexical_derivations then return nil end

  paragraphs_checked = paragraphs_checked + 1
  local seen = {}

  for i, inline in ipairs(el.content) do
    local form = nil

    if inline.t == 'Emph' then
      -- Plain Markdown italic: the primary source of lexical forms in Part I prose.
      emph_occurrences = emph_occurrences + 1
      form = utils.stringify(inline)

    elseif inline.t == 'Span' then
      if span_has_class(inline, 'pred') then
        -- .pred spans are counterfactual forms; they do not require glosses.
        -- Do not descend.
      elseif span_has_class(inline, 'iv') then
        -- .iv spans are indexed lexical forms; check them like plain Emph.
        emph_occurrences = emph_occurrences + 1
        form = form_from_iv_span(inline)
      end
      -- Other Span types: ignore.
    end

    if form and is_lexical(form) then
      local norm = normalize(form)
      if norm ~= '' and not seen[norm] then
        seen[norm] = true
        first_occurrence_candidates = first_occurrence_candidates + 1
        if not has_gloss_after(el.content, i) then
          table.insert(failures, { para = paragraphs_checked, form = form })
        end
      end
    end
  end

  return nil
end

function Pandoc(doc)
  local summary = string.format(
    'Paragraph gloss validator: %d violation(s) in %d prose paragraphs; '
    .. '%d Emph occurrences; %d first-occurrence candidates.\n',
    #failures, paragraphs_checked, emph_occurrences, first_occurrence_candidates
  )
  io.stderr:write(summary)
  if #failures > 0 then
    for _, f in ipairs(failures) do
      io.stderr:write(
        string.format('  Para %d: missing gloss for *%s*\n', f.para, f.form)
      )
    end
    os.exit(2)
  end
  return nil
end
