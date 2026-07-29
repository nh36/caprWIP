-- paragraph_gloss_validator.lua
-- Validation-only Pandoc Lua filter.
--
-- Part I (sound-change chapters):
--   Checks plain Emph, .iv spans, and .recon spans.
--   First occurrence of each lexical form in a Para must have an immediate gloss.
--   .pred spans are exempt.
--
-- Part II (lexical derivations):
--   Walks TOP-LEVEL blocks only (not table-cell Para elements).
--   Within reader-facing prose subsections (see PROSE_SECTIONS below):
--     checks Emph, Code, .iv, and .recon spans.
--   Outside those sections: checks .recon only.
--   .pred spans are always exempt.
--
-- Backmatter (references, indexes): skipped entirely.

local pandoc = require 'pandoc'
local utils  = pandoc.utils

-- ── state ────────────────────────────────────────────────────────────────────

local failures_p1 = {}
local failures_p2 = {}

local paras_p1     = 0;  local paras_p2       = 0
-- Part I counters
local emph_p1      = 0;  local cands_p1       = 0
-- Part II counters (by category)
local recon_p2     = 0;  local iv_p2          = 0;  local plain_p2 = 0; local code_p2 = 0
local cands_p2     = 0

local current_part    = "part1"
local p2_section      = ""    -- current Part II subsection heading text

-- ── Part II prose section allowlist ──────────────────────────────────────────
-- Only check Emph / .iv / .recon in these Part II subsections.
-- Other subsections (derivation traces, tables, summary lines) are excluded
-- from ordinary-form checking; .recon is still checked everywhere.

local PROSE_SECTIONS = {
  ["Reconstruction and comparative evidence"] = true,
  ["Old English evidence"]                    = true,
  ["Development to Old English"]              = true,
  ["Development note"]                        = true,
  ["Form note"]                               = true,
  ["Dialect note"]                            = true,
  ["Lexical note"]                            = true,
  ["Source note"]                             = true,
  ["Comparison note"]                         = true,
  ["Attestation note"]                        = true,
  ["Reconstruction status"]                   = true,
  ["What remains unexplained"]                = true,
  ["Expected and attested forms"]             = true,
  ["Formation comparison"]                    = true,
  ["Class comparison"]                        = true,
  ["Stage comparison"]                        = true,
  ["Stem comparison"]                         = true,
  ["Branch comparison"]                       = true,
  ["Alternant comparison"]                    = true,
  ["Source comparison"]                       = true,
  ["Paradigm-cell comparison"]                = true,
  ["Verb-family comparison"]                  = true,
  ["Stem and stage comparison"]               = true,
  ["Paradigm comparison"]                     = true,
  ["Variant comparison"]                      = true,
}

-- ── helpers ───────────────────────────────────────────────────────────────────

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

-- Count Unicode codepoints in a UTF-8 string (Lua's # operator counts bytes).
local function utf8_len(s)
  local count = 0
  local i = 1
  while i <= #s do
    local byte = s:byte(i)
    if byte >= 0xF0 then i = i + 4
    elseif byte >= 0xE0 then i = i + 3
    elseif byte >= 0xC0 then i = i + 2
    else i = i + 1 end
    count = count + 1
  end
  return count
end

local function has_non_ascii(s)
  for i = 1, #s do
    if s:byte(i) > 127 then return true end
  end
  return false
end

local function looks_like_linguistic_form(form)
  if not form or form == "" then return false end
  if form:sub(1,1) == "*" then return true end
  if has_non_ascii(form) then return true end
  if form:find("[-þðæǣġċīōūȳáéíóúý]") then return true end
  return false
end

-- Explicit set of phonological/diphthong sequences that must not become lexical
-- candidates even when italicised. These are vowel sequences, diphthong quality
-- labels, and similar non-lexical objects used in handbook notation.
-- Entries include both plain and asterisk-prefixed forms.
-- Regression fixtures: ēo → ignored; ēa → ignored; *ai → ignored; cū → checked.
local PHONOLOGICAL_SEQUENCES = {}
do
  local seqs = {
    -- OE vowel quality / diphthong notation (plain and long-vowel variants)
    "eo", "ea", "ie", "io", "ia", "oe",
    "ēo", "ēa", "īe", "ōe",
    -- PGmc/NWGmc diphthong source sequences
    "ai", "au", "ei", "eu", "iu", "ui", "oi", "ou",
    "āi", "āu", "ēi", "ēu",
    -- Common phonological cluster abbreviations (all ASCII, 2 letters)
    "lþ", "rþ", "nþ", "ng", "gg", "kk", "pp", "tt", "mm", "nn",
    "ll", "rr", "ss", "ff",
  }
  for _, s in ipairs(seqs) do
    PHONOLOGICAL_SEQUENCES[s] = true
    PHONOLOGICAL_SEQUENCES["*" .. s] = true
  end
end

-- Return true if this form looks like a segmental/stem notation rather than
-- a full lexical item that deserves a gloss.
local function is_notation_only(form)
  if not form or form == "" then return true end
  -- Explicit phonological sequences (vowel diphthongs, clusters)
  if PHONOLOGICAL_SEQUENCES[form] then return true end
  -- Strip leading asterisk for analysis
  local bare = form:gsub("^%*+", "")
  -- Trailing or leading hyphen → stem or affix notation
  if bare:sub(-1) == "-" or bare:sub(1,1) == "-" then return true end
  -- Uppercase singleton environment labels like C, V (in *rC, *VC notation)
  if bare:match("^.?[A-Z]$") then return true end
  -- Forms containing a comma are lists or multi-word strings, not single forms
  if form:find(",") then return true end
  -- Forms containing a space (multi-word phrase) are not single lexical items
  if form:find(" ") then return true end
  -- Forms containing a quote character internally already contain a gloss
  if form:find("'") then return true end
  if form:find("\xe2\x80\x98") or form:find("\xe2\x80\x99") then return true end
  -- Parenthetical alternate forms like *(j)ō, *kō- – contain parens or slashes
  if bare:match("[%(%)/%~%<%>]") then return true end
  -- Mixed- or upper-case rule labels / abbreviations (e.g. OEIUmlaut, PGmc)
  if bare:match("^[A-Z][A-Za-z]+$") then return true end
  -- Single Unicode codepoint
  local bare_len = utf8_len(bare)
  if bare_len <= 1 then return true end
  -- Short asterisked forms (≤2 codepoints) are phonological segments/sequences
  -- (e.g., *u, *z, *ō, *ai, *lþ). Non-asterisked short forms like cū, bā
  -- may be real OE words; allow them through.
  if form:sub(1,1) == "*" and bare_len <= 2 then return true end
  -- Pure ASCII 2-codepoint forms without asterisk are phonological clusters.
  if bare_len == 2 and not has_non_ascii(bare) then return true end
  return false
end

-- ── paragraph checker ─────────────────────────────────────────────────────────

local function check_para(el, is_p2, in_prose_section)
  if is_p2 then paras_p2 = paras_p2 + 1 else paras_p1 = paras_p1 + 1 end

  local seen = {}

  for i, inline in ipairs(el.content) do
    local form     = nil
    local category = nil   -- "emph", "iv", or "recon"

    if inline.t == 'Emph' then
      if not is_p2 then
        -- Part I: always check plain italic
        local f = utils.stringify(inline)
        if looks_like_linguistic_form(f) then
          emph_p1 = emph_p1 + 1
          form = f
          category = "emph"
        end
      elseif in_prose_section then
        -- Part II prose sections: check plain italic
        local f = utils.stringify(inline)
        if looks_like_linguistic_form(f) and not is_notation_only(f) then
          plain_p2 = plain_p2 + 1
          form = f
          category = "emph"
        end
      end

    elseif inline.t == 'Code' then
      if is_p2 and in_prose_section then
        local f = inline.text
        if not is_notation_only(f) then
          code_p2 = code_p2 + 1
          form = f
          category = "code"
        end
      elseif not is_p2 then
        local f = inline.text
        -- Part I: Code spans are used for rule names and phonological notation.
        -- Only check Code spans that contain non-ASCII characters (genuine PGmc/OE
        -- lexical forms with diacritics); pure-ASCII Code spans (*ijo, *iu, rule
        -- identifiers) are phonological or rule notation and are excluded.
        if has_non_ascii(f) and looks_like_linguistic_form(f) and not is_notation_only(f) then
          emph_p1 = emph_p1 + 1
          form = f
          category = "code"
        end
      end

    elseif inline.t == 'Span' then
      if span_has_class(inline, 'pred') then
        -- always exempt
      elseif span_has_class(inline, 'recon') then
        -- .recon: check in all sections (Part I and Part II)
        if is_p2 then recon_p2 = recon_p2 + 1 else emph_p1 = emph_p1 + 1 end
        local f = form_from_span(inline)
        if not is_notation_only(f) then
          form = f; category = "recon"
        end
      elseif span_has_class(inline, 'iv') then
        if not is_p2 then
          -- Part I: check .iv
          emph_p1 = emph_p1 + 1
          form = form_from_span(inline); category = "iv"
        elseif in_prose_section then
          -- Part II prose sections: check .iv
          -- Skip combined .recon+.iv spans — the gloss is inside the span itself
          local has_inner_recon = false
          for _, ch in ipairs(inline.content) do
            if ch.t == 'Span' and span_has_class(ch, 'recon') then
              has_inner_recon = true; break
            end
          end
          if not has_inner_recon then
            iv_p2 = iv_p2 + 1
            local f = form_from_span(inline)
            if not is_notation_only(f) then
              form = f; category = "iv"
            end
          end
        end
      end
    end

    if form and form ~= "" then
      local norm = normalize(form)
      if norm ~= "" and not seen[norm] then
        seen[norm] = true
        if is_p2 then cands_p2 = cands_p2 + 1 else cands_p1 = cands_p1 + 1 end
        if not has_gloss_after(el.content, i) then
          local entry = {
            para    = (is_p2 and paras_p2 or paras_p1),
            form    = form,
            cat     = category,
            section = p2_section,
          }
          if is_p2 then table.insert(failures_p2, entry)
          else          table.insert(failures_p1, entry) end
        end
      end
    end
  end
end

-- ── document walker ───────────────────────────────────────────────────────────
-- Walk only TOP-LEVEL blocks.  This means Para elements inside Table cells
-- are never visited, avoiding false positives from structured data rows.

local function process_blocks(blocks)
  for _, block in ipairs(blocks) do
    if block.t == 'Header' then
      local t = utils.stringify(block)
      -- Part tracking (level-1 or level-2 headings that demarcate parts)
      if t == 'Word-by-word derivations' then
        current_part = "part2"
        p2_section   = ""
      elseif t == 'References' or t == 'Index verborum' then
        current_part = "back"
        p2_section   = ""
      elseif current_part == "part2" and block.level >= 3 then
        -- Level-4 headings name the subsections within each entry
        p2_section = t
      end

    elseif block.t == 'Para' then
      if current_part == "part1" then
        check_para(block, false, false)
      elseif current_part == "part2" then
        local in_prose = PROSE_SECTIONS[p2_section] or false
        check_para(block, true, in_prose)
      end
      -- "back" → skip

    elseif block.t == 'Div' or block.t == 'BlockQuote' then
      -- Recurse into div/blockquote (rare in this document, but be safe)
      if current_part ~= "back" then
        process_blocks(block.content)
      end

    -- Table, RawBlock, CodeBlock, BulletList, OrderedList: skip
    -- (Table cells have their own nested Para elements that we intentionally
    --  do not visit here; raw TeX blocks are derivation traces.)
    end
  end
end

-- ── entry point ───────────────────────────────────────────────────────────────

function Pandoc(doc)
  process_blocks(doc.blocks)

  local total = #failures_p1 + #failures_p2
  io.stderr:write(string.format(
    'Paragraph gloss validator:\n'
    ..'  Part I:  %d prose paragraphs, %d Emph/iv/recon occurrences, %d first-occurrence candidates, %d violation(s)\n'
    ..'  Part II: %d prose paragraphs in scope, %d .recon, %d .iv, %d plain-italic, %d code occurrences, %d first-occurrence candidates, %d violation(s)\n'
    ..'  Total violations: %d\n',
    paras_p1, emph_p1, cands_p1, #failures_p1,
    paras_p2, recon_p2, iv_p2, plain_p2, code_p2, cands_p2, #failures_p2,
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
        io.stderr:write(string.format('    Para %d [%s]: missing gloss for *%s* (%s)\n',
          f.para, f.section, f.form, f.cat))
      end
    end
    os.exit(2)
  end
  return nil
end
