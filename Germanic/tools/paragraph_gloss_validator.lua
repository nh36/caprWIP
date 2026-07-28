-- paragraph_gloss_validator.lua
-- Validation-only Pandoc Lua filter.
--
-- Part I (sound-change chapters):
--   Checks plain Emph, .iv spans, and .recon spans.
--   First occurrence of each lexical form in a Para must have an immediate gloss.
--   .pred spans are exempt.
--
-- Part II (lexical derivations):
--   Checks .recon spans only.
--   .iv PGmc data fields and short structured-data Para blocks are common;
--   restricting to .recon catches only explicitly-authored reconstructed prose.
--
-- Backmatter (references, indexes): skipped entirely.

local pandoc = require 'pandoc'
local utils  = pandoc.utils

local failures_p1 = {}
local failures_p2 = {}

local paras_p1 = 0; local paras_p2 = 0
local emph_p1  = 0; local emph_p2  = 0
local cands_p1 = 0; local cands_p2 = 0

local current_part = "part1"

-- ── helpers ──────────────────────────────────────────────────────────────────

local function normalize(s)
  return (string.lower(s):gsub("[^%w]", ""))
end

local function starts_with_opening_quote(text)
  if not text or text == "" then return false end
  local b1 = text:byte(1)
  if b1 == 0x27 or b1 == 0x22 or b1 == 0x60 then return true end
  if b1 == 0xE2 and #text >= 3 then
    local b2 = text:byte(2); local b3 = text:byte(3)
    if b2 == 0x80 and (b3 == 0x98 or b3 == 0x99 or b3 == 0x9C or b3 == 0x9D) then
      return true
    end
  end
  return false
end

local function has_gloss_after(content, idx)
  local j = idx + 1
  while j <= #content do
    local nxt = content[j]
    if nxt.t == 'Space' or nxt.t == 'SoftBreak' then
      j = j + 1
    elseif nxt.t == 'Str'    then return starts_with_opening_quote(nxt.text)
    elseif nxt.t == 'Quoted' then return true
    else                          return false
    end
  end
  return false
end

local function span_has_class(span, cls)
  if not span.classes then return false end
  for _, c in ipairs(span.classes) do if c == cls then return true end end
  return false
end

-- Extract italic inner text from a span; fall back to full stringify.
local function form_from_span(span)
  for _, ch in ipairs(span.content) do
    if ch.t == 'Emph' then return utils.stringify(ch) end
  end
  return utils.stringify(span)
end

-- ── part tracking ─────────────────────────────────────────────────────────────

function Header(el)
  local t = utils.stringify(el)
  if t == 'Word-by-word derivations' then current_part = "part2"
  elseif t == 'References' or t == 'Index verborum' then current_part = "back"
  end
  return nil
end

-- ── paragraph check ───────────────────────────────────────────────────────────

function Para(el)
  if current_part == "back" then return nil end

  local is_p2 = (current_part == "part2")
  if is_p2 then paras_p2 = paras_p2 + 1 else paras_p1 = paras_p1 + 1 end

  local seen = {}

  for i, inline in ipairs(el.content) do
    local form = nil

    if inline.t == 'Emph' then
      -- Part I: plain italic is a candidate.  Part II: skip (noisy data fields).
      if not is_p2 then
        emph_p1 = emph_p1 + 1
        form = utils.stringify(inline)
      end

    elseif inline.t == 'Span' then
      if span_has_class(inline, 'pred') then
        -- exempt — skip
      elseif span_has_class(inline, 'recon') then
        -- Both parts: .recon is explicitly authored reconstruction markup.
        if is_p2 then emph_p2 = emph_p2 + 1 else emph_p1 = emph_p1 + 1 end
        form = form_from_span(inline)
      elseif span_has_class(inline, 'iv') and not is_p2 then
        -- Part I only: .iv lexical spans.
        emph_p1 = emph_p1 + 1
        form = form_from_span(inline)
      end
    end

    if form and form ~= "" then
      local norm = normalize(form)
      if norm ~= "" and not seen[norm] then
        seen[norm] = true
        if is_p2 then cands_p2 = cands_p2 + 1 else cands_p1 = cands_p1 + 1 end
        if not has_gloss_after(el.content, i) then
          local entry = { para = (is_p2 and paras_p2 or paras_p1), form = form }
          if is_p2 then table.insert(failures_p2, entry)
          else          table.insert(failures_p1, entry) end
        end
      end
    end
  end
  return nil
end

-- ── summary ───────────────────────────────────────────────────────────────────

function Pandoc(doc)
  local total = #failures_p1 + #failures_p2
  io.stderr:write(string.format(
    'Paragraph gloss validator:\n'
    ..'  Part I:  %d prose paragraphs, %d Emph occurrences, %d first-occurrence candidates, %d violation(s)\n'
    ..'  Part II: %d prose paragraphs, %d .recon occurrences, %d first-occurrence candidates, %d violation(s)\n'
    ..'  Total violations: %d\n',
    paras_p1, emph_p1, cands_p1, #failures_p1,
    paras_p2, emph_p2, cands_p2, #failures_p2,
    total))
  if total > 0 then
    if #failures_p1 > 0 then
      io.stderr:write('  Part I violations:\n')
      for _, f in ipairs(failures_p1) do
        io.stderr:write(string.format('    Para %d: missing gloss for *%s*\n', f.para, f.form))
      end
    end
    if #failures_p2 > 0 then
      io.stderr:write('  Part II violations:\n')
      for _, f in ipairs(failures_p2) do
        io.stderr:write(string.format('    Para %d: missing gloss for *%s*\n', f.para, f.form))
      end
    end
    os.exit(2)
  end
  return nil
end
