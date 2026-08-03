local PRINT_MAIN_TSV = os.getenv("CAPR_IV_PRINT_MAIN_TSV") or "Germanic/docs/book/index_verborum_print_main.tsv"
local LANGUAGE_REGISTRY_TSV = os.getenv("CAPR_IV_LANGUAGE_REGISTRY_TSV") or "Germanic/docs/book/index_verborum_languages.tsv"
local VARIETY_REGISTRY_TSV = os.getenv("CAPR_IV_VARIETY_REGISTRY_TSV") or "Germanic/docs/book/index_verborum_varieties.tsv"
local BOOK_EMISSIONS_TSV = os.getenv("CAPR_IV_BOOK_EMISSIONS_TSV") or "Germanic/docs/book/index_verborum_book_emissions.tsv"
local lang_meta = nil  -- {code → {order_str, title, escaped_title}}
local variety_meta = nil  -- {code → {printed_label, display_order, assignable, active, language, suppress}}
local explicit_allow = nil
-- ── Emission plan (for .iv-anchor path) ───────────────────────────────────────
-- emission_plan[emission_id] = precomputed_index_command
-- Loaded lazily when the first .iv-anchor span or div is encountered.
local emission_plan = nil        -- emission_id → index_command
local occurrence_to_emission = nil  -- occurrence_id → emission_id

-- ── Targeted canonical composition for Index Verborum matching ────────────────
-- This helper performs targeted canonical composition for the OE diacritic
-- repertoire required by the Index Verborum corpus. It composes the specific
-- NFD sequences (base character + combining diacritic) that occur in corpus
-- forms into their NFC precomposed equivalents.
--
-- This is NOT a general Unicode NFC normalization library. Combining sequences
-- that are not present in the Old English corpus pass through unchanged.
--
-- Current coverage:
--   combining macron (U+0304): a e i o u y æ (and capitals) → ā ē ī ō ū ȳ ǣ etc.
--   combining dot above (U+0307): c g s w (and capitals) → ċ ġ ṡ ẇ etc.
--
-- Both TSV-loaded values and Pandoc-stringified span content are passed through
-- this helper before the eligibility key comparison, making primary matching
-- robust to NFD/NFC source-file variation without a sort-key fallback.
local IV_MATCH_WIDE = {
  -- æ/Æ + combining macron  (4-byte NFD → 2-byte NFC)
  ["\xc3\xa6\xcc\x84"] = "\xc7\xa3",  -- ǣ U+01E3
  ["\xc3\x86\xcc\x84"] = "\xc7\xa2",  -- Ǣ U+01E2
}
local IV_MATCH_NARROW = {
  -- vowel + combining macron (3-byte NFD → 2-byte NFC)
  ["\x61\xcc\x84"] = "\xc4\x81",  -- ā U+0101
  ["\x65\xcc\x84"] = "\xc4\x93",  -- ē U+0113
  ["\x69\xcc\x84"] = "\xc4\xab",  -- ī U+012B
  ["\x6f\xcc\x84"] = "\xc5\x8d",  -- ō U+014D
  ["\x75\xcc\x84"] = "\xc5\xab",  -- ū U+016B
  ["\x79\xcc\x84"] = "\xc8\xb3",  -- ȳ U+0233
  ["\x41\xcc\x84"] = "\xc4\x80",  -- Ā U+0100
  ["\x45\xcc\x84"] = "\xc4\x92",  -- Ē U+0112
  ["\x49\xcc\x84"] = "\xc4\xaa",  -- Ī U+012A
  ["\x4f\xcc\x84"] = "\xc5\x8c",  -- Ō U+014C
  ["\x55\xcc\x84"] = "\xc5\xaa",  -- Ū U+016A
  ["\x59\xcc\x84"] = "\xc8\xb2",  -- Ȳ U+0232
  -- consonant + combining dot above (3-byte NFD → 2/3-byte NFC)
  ["\x63\xcc\x87"] = "\xc4\x8b",      -- ċ U+010B
  ["\x67\xcc\x87"] = "\xc4\xa1",      -- ġ U+0121
  ["\x43\xcc\x87"] = "\xc4\x8a",      -- Ċ U+010A
  ["\x47\xcc\x87"] = "\xc4\xa0",      -- Ġ U+0120
  ["\x73\xcc\x87"] = "\xe1\xb9\xa1",  -- ṡ U+1E61
  ["\x77\xcc\x87"] = "\xe1\xba\x87",  -- ẇ U+1E87
  ["\x53\xcc\x87"] = "\xe1\xb9\xa0",  -- Ṡ U+1E60
  ["\x57\xcc\x87"] = "\xe1\xba\x86",  -- Ẇ U+1E86
}

local function normalize_iv_match_text(s)
  -- Apply multi-byte-base patterns first (æ/Æ+macron) to avoid partial
  -- replacement of their ASCII tail bytes by the narrow table.
  for nfd, nfc in pairs(IV_MATCH_WIDE) do
    s = s:gsub(nfd, nfc)
  end
  for nfd, nfc in pairs(IV_MATCH_NARROW) do
    s = s:gsub(nfd, nfc)
  end
  return s
end

local function trim(value)
  return (value or ""):gsub("^%s+", ""):gsub("%s+$", "")
end

local function split_tsv(line)
  local cells = {}
  local start_at = 1
  while true do
    local tab = line:find("\t", start_at, true)
    if tab then
      table.insert(cells, line:sub(start_at, tab - 1))
      start_at = tab + 1
    else
      table.insert(cells, line:sub(start_at))
      break
    end
  end
  return cells
end

local function column(cells, idx)
  if not idx then
    return ""
  end
  return trim(cells[idx] or "")
end

local function explicit_key(language, role, value, source_ref, variety)
  return (language or "") .. "\t" .. (role or "") .. "\t" .. (value or "") .. "\t" .. (source_ref or "") .. "\t" .. (variety or "")
end

local function ensure_variety_meta_loaded()
  if variety_meta ~= nil then return variety_meta end
  variety_meta = {}
  local handle = io.open(VARIETY_REGISTRY_TSV, "r")
  if not handle then
    error("index_verborum_filter.lua: cannot read " .. VARIETY_REGISTRY_TSV)
  end
  local header_line = handle:read("*l")
  if not header_line then handle:close(); return variety_meta end
  local headers = {}
  local s = 1
  while true do
    local t = header_line:find("\t", s, true)
    if t then table.insert(headers, header_line:sub(s, t-1)); s = t+1
    else table.insert(headers, header_line:sub(s)); break end
  end
  local idx = {}
  for i, h in ipairs(headers) do idx[trim(h)] = i end
  for line in handle:lines() do
    if line ~= "" then
      local cells = {}
      local c = 1
      while true do
        local t = line:find("\t", c, true)
        if t then table.insert(cells, line:sub(c, t-1)); c = t+1
        else table.insert(cells, line:sub(c)); break end
      end
      local code = trim(cells[idx["code"]] or "")
      if code ~= "" then
        variety_meta[code] = {
          language = trim(cells[idx["language"]] or ""),
          printed_label = trim(cells[idx["printed_label"]] or ""),
          display_order = tonumber((trim(cells[idx["display_order"]] or "0"))) or 0,
          suppress = trim(cells[idx["suppress_label"]] or "") == "1",
          assignable = trim(cells[idx["assignable"]] or "") == "1",
          active = trim(cells[idx["active"]] or "") == "1",
        }
      end
    end
  end
  handle:close()
  return variety_meta
end

-- Fail-closed validation of a nonblank occurrence variety; returns printed label.
local function validate_variety(language, variety)
  if variety == "" then return "" end
  local meta = ensure_variety_meta_loaded()
  local entry = meta[variety]
  if not entry then
    error("index_verborum_filter.lua: unknown variety '" .. variety .. "'")
  end
  if not entry.active then
    error("index_verborum_filter.lua: inactive variety '" .. variety .. "'")
  end
  if not entry.assignable then
    error("index_verborum_filter.lua: non-assignable variety '" .. variety .. "' (e.g. 'ws')")
  end
  if entry.language ~= language then
    error("index_verborum_filter.lua: variety '" .. variety .. "' not valid for language '" .. (language or "") .. "'")
  end
  if entry.suppress then return "" end
  return entry.printed_label
end

local function ensure_lang_meta_loaded()
  if lang_meta ~= nil then return lang_meta end
  lang_meta = {}
  local order = 0
  local handle = io.open(LANGUAGE_REGISTRY_TSV, "r")
  if not handle then
    error("index_verborum_filter.lua: cannot read " .. LANGUAGE_REGISTRY_TSV)
  end
  local header_line = handle:read("*l")
  if not header_line then handle:close(); return lang_meta end
  -- parse header to find column indices
  local headers = {}
  local start_at = 1
  while true do
    local tab = header_line:find("\t", start_at, true)
    if tab then
      table.insert(headers, header_line:sub(start_at, tab-1))
      start_at = tab + 1
    else
      table.insert(headers, header_line:sub(start_at))
      break
    end
  end
  local code_idx, title_idx, active_idx, note_idx = nil, nil, nil, nil
  for i, h in ipairs(headers) do
    if h == "code" then code_idx = i
    elseif h == "title" then title_idx = i
    elseif h == "active" then active_idx = i
    elseif h == "index_note" then note_idx = i
    end
  end
  for line in handle:lines() do
    if line ~= "" then
      local cells = {}
      local s = 1
      while true do
        local t = line:find("\t", s, true)
        if t then table.insert(cells, line:sub(s, t-1)); s = t+1
        else table.insert(cells, line:sub(s)); break end
      end
      local code = trim(cells[code_idx] or "")
      local title = trim(cells[title_idx] or "")
      local active = trim(cells[active_idx] or "")
      local note = note_idx and trim(cells[note_idx] or "") or ""
      if code ~= "" and active == "1" then
        order = order + 1
        local order_str = string.format("%02d", order)
        -- escape @ and ! for MakeIndex; include the optional reader-facing note
        -- as the second \ivlangheader argument so Python and Lua stay equivalent.
        local escaped = title:gsub("@", "\\@"):gsub("!", "\\!")
        local escaped_note = note:gsub("@", "\\@"):gsub("!", "\\!")
        lang_meta[code] = {order_str = order_str .. code, title = title, escaped_title = "\\ivlangheader{" .. escaped .. "}{" .. escaped_note .. "}"}
      end
    end
  end
  handle:close()
  return lang_meta
end

local function ensure_print_main_loaded()
  if explicit_allow ~= nil then
    return explicit_allow
  end
  explicit_allow = {}
  local handle = io.open(PRINT_MAIN_TSV, "r")
  if not handle then
    error("index_verborum_filter.lua: cannot read " .. PRINT_MAIN_TSV .. "; run build_index_verborum.py first.")
  end
  local header_line = handle:read("*l")
  if not header_line then
    handle:close()
    error("index_verborum_filter.lua: missing header in " .. PRINT_MAIN_TSV)
  end
  local headers = split_tsv(header_line)
  local indices = {}
  for i, name in ipairs(headers) do
    indices[name] = i
  end
  for _, required in ipairs({ "language", "form", "display", "form_role", "source_scope", "source_ref" }) do
    if not indices[required] then
      handle:close()
      error("index_verborum_filter.lua: missing required column '" .. required .. "' in " .. PRINT_MAIN_TSV)
    end
  end
  for line in handle:lines() do
    if line ~= "" then
      local cells = split_tsv(line)
      if column(cells, indices["source_scope"]) == "explicit_tag" then
        local language = column(cells, indices["language"])
        local role = column(cells, indices["form_role"])
        local form = normalize_iv_match_text(column(cells, indices["form"]))
        local display = normalize_iv_match_text(column(cells, indices["display"]))
        local source_ref = column(cells, indices["source_ref"])
        local variety = column(cells, indices["variety"])
        if role == "" then
          role = "evidence_form"
        end
        explicit_allow[explicit_key(language, role, form, source_ref, variety)] = true
        explicit_allow[explicit_key(language, role, display, source_ref, variety)] = true
      end
    end
  end
  handle:close()
  return explicit_allow
end

local function has_class(el, class_name)
  for _, class in ipairs(el.classes) do
    if class == class_name then
      return true
    end
  end
  return false
end

local function latex_escape(value)
  return value:gsub("([@!|])", "\\%1")
end

local function italicize_oe_content(content)
  if #content == 1 and content[1].t == "Emph" then
    return content
  end
  local visible = {}
  for _, inline in ipairs(content) do
    table.insert(visible, inline.t == "Code" and pandoc.Str(inline.text) or inline)
  end
  return { pandoc.Emph(visible) }
end

local function visible_span(span)
  local filtered_classes = {}
  for _, class in ipairs(span.classes) do
    if class ~= "iv" then
      table.insert(filtered_classes, class)
    end
  end
  local filtered_attrs = {}
  for key, value in pairs(span.attributes) do
    if key ~= "lang" and key ~= "sort" and key ~= "display" and key ~= "source_scope" and key ~= "source_ref" and key ~= "role" and key ~= "variety" and key ~= "occ_id" then
      filtered_attrs[key] = value
    end
  end
  local content = span.content
  if trim(span.attributes["lang"] or "") == "oe" then
    content = italicize_oe_content(content)
  end
  return pandoc.Span(content, pandoc.Attr(span.identifier, filtered_classes, filtered_attrs))
end

local function explicit_tag_is_printable(language, role, form, display, source_ref, variety)
  if language == "" then
    return false
  end
  -- Note: preoe forms are now allowed to print if they appear in print_main.
  -- The blanket preoe exclusion was removed (§11 fix); use print_main as the authority.
  local allow = ensure_print_main_loaded()
  if source_ref == "" then
    return false
  end
  -- Primary check: form/display-based
  if allow[explicit_key(language, role, form, source_ref, variety)]
      or allow[explicit_key(language, role, display, source_ref, variety)] then
    return true
  end
  return false
end

local function span_to_index(span)
  if not has_class(span, "iv") then
    return span
  end
  local visible = visible_span(span)
  local lang = trim(span.attributes["lang"] or "")
  if lang == "" then
    return visible
  end
  local role = trim(span.attributes["role"] or "")
  if role == "" then
    role = "evidence_form"
  end
  local source_ref = trim(span.attributes["source_ref"] or "")
  local occ_id = trim(span.attributes["occ_id"] or "")
  local variety = trim(span.attributes["variety"] or "")
  -- Fail-closed validation; also yields the printed label (blank => no suffix).
  local variety_label = validate_variety(lang, variety)
  local form = normalize_iv_match_text(trim(pandoc.utils.stringify(span.content)))
  local display_attr = normalize_iv_match_text(trim(span.attributes["display"] or ""))
  -- A combined .recon .iv span carries reconstruction semantics; derive the starred
  -- display automatically when no explicit display= attribute is provided.
  local is_recon = has_class(span, "recon")
  local display = display_attr ~= "" and display_attr or (is_recon and ("*" .. form) or form)
  -- Strip trailing reconstruction asterisk after a stem hyphen (e.g. *hemina-* → *hemina-).
  -- This matches the normalize_print_text stripping applied on the Python side so that
  -- Kroonen-style stem entries (marked *stem-*) display consistently without the trailing *.
  display = display:gsub("(%*[^%s`|<>]-%-?)%*$", "%1"):gsub("(%*[^%s`|<>]-%-?)%*([`_%.,%s;:!?)/%]%}>~])", "%1%2")
  -- Sort key must always derive from the bare (unstarred) form, not from the display.
  -- A starred display would otherwise propagate a leading asterisk into the sort key.
  local sort = trim(span.attributes["sort"] or form)
  -- Check printability by canonical explicit allowlist.
  local printable = explicit_tag_is_printable(lang, role, form, display, source_ref, variety)
  if not printable then return visible end
  -- Every language's form is italicized through the general \iventry macro; the
  -- optional variety label (Old English only, at present) is printed in roman.
  local index_display = "\\iventry{" .. latex_escape(display) .. "}{" .. variety_label .. "}"
  -- Hidden MakeIndex discriminator (collision-proof): a labelled variety appends
  -- "~" + two-digit display_order to the sort field only. "~" can never appear
  -- in a scholarly sort key ([a-z0-9]), so the mapping stays injective and blank
  -- (real corpus) entries sort first as strict prefixes. Mirrors the Python
  -- DISCRIMINATOR_SEP in index_verborum_render.py.
  local escaped_sort = latex_escape(sort)
  local disc = ""
  if variety ~= "" then
    if escaped_sort:find("~", 1, true) then
      error("index_verborum_filter.lua: sort key '" .. sort .. "' contains reserved discriminator separator '~'")
    end
    local vmeta = ensure_variety_meta_loaded()
    local ventry = vmeta[variety]
    if ventry then
      disc = "~" .. string.format("%02d", ventry.display_order)
    end
  end
  local meta = ensure_lang_meta_loaded()
  local lm = meta[lang]
  local lang_sort = lm and lm.order_str or ("99" .. lang)
  local lang_display = lm and lm.escaped_title or ("\\ivlangheader{" .. lang .. "}{}")
  local raw = pandoc.RawInline("latex", "\\index[iv]{" .. lang_sort .. "@" .. lang_display .. "!" .. escaped_sort .. disc .. "@" .. index_display .. "}")
  return { visible, raw }
end

-- ── Emission-plan loader ──────────────────────────────────────────────────────
-- Loads index_verborum_book_emissions.tsv and validates the data fail-closed.
-- Called lazily the first time an .iv-anchor span or div is encountered.
--
-- Accepted emission_path values:
--   explicit_tag
--   heading_injection
--   line_injection
--
-- The precomputed index_command is stored verbatim; Lua does NOT reconstruct it.
local ACCEPTED_EMISSION_PATHS = {
  explicit_tag = true,
  heading_injection = true,
  line_injection = true,
}

local function ensure_emission_plan_loaded()
  if emission_plan ~= nil then
    return emission_plan
  end
  emission_plan = {}
  occurrence_to_emission = {}

  local handle = io.open(BOOK_EMISSIONS_TSV, "r")
  if not handle then
    error("index_verborum_filter.lua: cannot read " .. BOOK_EMISSIONS_TSV
          .. "; run build_index_verborum.py and index_verborum_emission.py first.")
  end

  local header_line = handle:read("*l")
  if not header_line then
    handle:close()
    error("index_verborum_filter.lua: " .. BOOK_EMISSIONS_TSV .. " is empty (no header).")
  end

  -- Parse header
  local headers = split_tsv(header_line)
  local idx = {}
  for i, h in ipairs(headers) do idx[trim(h)] = i end

  local required_columns = {
    "emission_id", "representative_occurrence_id", "emission_path",
    "index_command", "source_occurrence_count", "source_occurrence_ids",
  }
  for _, col in ipairs(required_columns) do
    if not idx[col] then
      handle:close()
      error("index_verborum_filter.lua: " .. BOOK_EMISSIONS_TSV
            .. " missing required column '" .. col .. "'")
    end
  end

  local all_occurrence_ids = {}  -- occurrence_id → emission_id, for duplicate detection
  local row_num = 1

  for line in handle:lines() do
    row_num = row_num + 1
    if line == "" then goto continue end
    local cells = split_tsv(line)

    local emission_id    = column(cells, idx["emission_id"])
    local rep_occ_id     = column(cells, idx["representative_occurrence_id"])
    local epath          = column(cells, idx["emission_path"])
    local index_command  = column(cells, idx["index_command"])
    local count_str      = column(cells, idx["source_occurrence_count"])
    local occ_ids_str    = column(cells, idx["source_occurrence_ids"])

    -- 1. Blank emission_id
    if emission_id == "" then
      handle:close()
      error("index_verborum_filter.lua: row " .. row_num
            .. " in " .. BOOK_EMISSIONS_TSV .. " has blank emission_id")
    end

    -- 2. Duplicate emission_id
    if emission_plan[emission_id] then
      handle:close()
      error("index_verborum_filter.lua: duplicate emission_id '" .. emission_id
            .. "' in " .. BOOK_EMISSIONS_TSV)
    end

    -- 3. Blank index_command
    if index_command == "" then
      handle:close()
      error("index_verborum_filter.lua: emission_id '" .. emission_id
            .. "' has blank index_command in " .. BOOK_EMISSIONS_TSV)
    end

    -- 4. Blank representative_occurrence_id
    if rep_occ_id == "" then
      handle:close()
      error("index_verborum_filter.lua: emission_id '" .. emission_id
            .. "' has blank representative_occurrence_id in " .. BOOK_EMISSIONS_TSV)
    end

    -- 5. Blank source_occurrence_ids
    if occ_ids_str == "" then
      handle:close()
      error("index_verborum_filter.lua: emission_id '" .. emission_id
            .. "' has blank source_occurrence_ids in " .. BOOK_EMISSIONS_TSV)
    end

    -- 6. Invalid or non-integer source_occurrence_count
    local count = tonumber(count_str)
    if not count or count ~= math.floor(count) or count < 1 then
      handle:close()
      error("index_verborum_filter.lua: emission_id '" .. emission_id
            .. "' has invalid source_occurrence_count '" .. count_str
            .. "' (must be positive integer) in " .. BOOK_EMISSIONS_TSV)
    end

    -- 7. Unsupported or blank emission_path
    if epath == "" or not ACCEPTED_EMISSION_PATHS[epath] then
      handle:close()
      error("index_verborum_filter.lua: emission_id '" .. emission_id
            .. "' has unsupported emission_path '" .. epath
            .. "' in " .. BOOK_EMISSIONS_TSV
            .. " (accepted: explicit_tag, heading_injection, line_injection)")
    end

    -- 8. Parse and validate occurrence IDs
    local occ_ids = {}
    local start_pos = 1
    while true do
      local pipe_pos = occ_ids_str:find("|", start_pos, true)
      if pipe_pos then
        local oid = (trim(occ_ids_str:sub(start_pos, pipe_pos - 1)))
        occ_ids[#occ_ids + 1] = oid
        start_pos = pipe_pos + 1
      else
        local oid = (trim(occ_ids_str:sub(start_pos)))
        occ_ids[#occ_ids + 1] = oid
        break
      end
    end

    -- 9. Count mismatch between source_occurrence_count and pipe-separated IDs
    if #occ_ids ~= count then
      handle:close()
      error("index_verborum_filter.lua: emission_id '" .. emission_id
            .. "' source_occurrence_count=" .. count_str
            .. " but found " .. #occ_ids
            .. " occurrence_ids in source_occurrence_ids (in " .. BOOK_EMISSIONS_TSV .. ")")
    end

    -- 10. Duplicate occurrence IDs within one emission
    local seen_within = {}
    for _, oid in ipairs(occ_ids) do
      if oid == "" then
        handle:close()
        error("index_verborum_filter.lua: emission_id '" .. emission_id
              .. "' has blank occurrence_id in source_occurrence_ids")
      end
      if seen_within[oid] then
        handle:close()
        error("index_verborum_filter.lua: emission_id '" .. emission_id
              .. "' has duplicate occurrence_id '" .. oid
              .. "' in source_occurrence_ids")
      end
      seen_within[oid] = true
    end

    -- 11. Representative must appear in source_occurrence_ids
    if not seen_within[rep_occ_id] then
      handle:close()
      error("index_verborum_filter.lua: emission_id '" .. emission_id
            .. "' representative_occurrence_id '" .. rep_occ_id
            .. "' does not appear in source_occurrence_ids")
    end

    -- 12. One occurrence_id must not map to more than one emission
    for _, oid in ipairs(occ_ids) do
      if all_occurrence_ids[oid] then
        handle:close()
        error("index_verborum_filter.lua: occurrence_id '" .. oid
              .. "' appears in both emission '" .. all_occurrence_ids[oid]
              .. "' and emission '" .. emission_id
              .. "' in " .. BOOK_EMISSIONS_TSV)
      end
      all_occurrence_ids[oid] = emission_id
    end

    -- Store validated entry
    emission_plan[emission_id] = index_command
    for _, oid in ipairs(occ_ids) do
      occurrence_to_emission[oid] = emission_id
    end

    ::continue::
  end
  handle:close()
  return emission_plan
end

-- ── .iv-anchor handler ────────────────────────────────────────────────────────
-- An .iv-anchor is a planned-emission anchor marker. It carries an emission_id
-- attribute that maps to a precomputed index_command in the emission plan.
--
-- Supported Pandoc forms:
--
--   Inline: []{.iv-anchor emission_id="emit:xxx"}
--   Block:  ::: {.iv-anchor emission_id="emit:xxx"}
--           :::
--
-- Both forms produce no visible output and emit the exact precomputed command.
-- The index_command is stored verbatim from the TSV; Lua does NOT reconstruct
-- it. This enforces the architectural contract that Python owns command
-- construction.
--
-- Fail-closed on unknown emission_id — a missing plan entry is a build error.

local function anchor_to_index_command(emission_id)
  if emission_id == nil or emission_id == "" then
    error("index_verborum_filter.lua: .iv-anchor span has blank emission_id")
  end
  local plan = ensure_emission_plan_loaded()
  local cmd = plan[emission_id]
  if cmd == nil then
    error("index_verborum_filter.lua: .iv-anchor emission_id '" .. emission_id
          .. "' not found in emission plan (" .. BOOK_EMISSIONS_TSV .. ")")
  end
  return pandoc.RawInline("latex", cmd)
end

local function span_is_anchor(span)
  for _, cls in ipairs(span.classes) do
    if cls == "iv-anchor" then return true end
  end
  return false
end

local function handle_anchor_span(span)
  if not span_is_anchor(span) then return nil end
  local emission_id = trim(span.attributes["emission_id"] or "")
  return { anchor_to_index_command(emission_id) }
end

local function div_is_anchor(div)
  for _, cls in ipairs(div.classes) do
    if cls == "iv-anchor" then return true end
  end
  return false
end

local function handle_anchor_div(div)
  if not div_is_anchor(div) then return nil end
  local emission_id = trim(div.attributes["emission_id"] or "")
  -- Block anchor emits as a paragraph containing the RawInline command,
  -- followed by no visible content.
  return pandoc.Plain({ anchor_to_index_command(emission_id) })
end

function Pandoc(doc)
  local blocks = {}
  for _, block in ipairs(doc.blocks) do
    if block.t == "Div" and block.identifier == "refs" then
      table.insert(blocks, block)
    elseif block.t == "Div" and div_is_anchor(block) then
      -- Block-level .iv-anchor: emit precomputed command, no visible output.
      table.insert(blocks, handle_anchor_div(block))
    else
      -- Walk sub-tree for both .iv spans and inline .iv-anchor spans.
      table.insert(blocks, block:walk({
        Span = function(span)
          if span_is_anchor(span) then
            return handle_anchor_span(span)
          end
          return span_to_index(span)
        end
      }))
    end
  end
  return pandoc.Pandoc(blocks, doc.meta)
end
