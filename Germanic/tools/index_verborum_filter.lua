local BOOK_EMISSIONS_TSV = os.getenv("CAPR_IV_BOOK_EMISSIONS_TSV") or "Germanic/docs/book/index_verborum_book_emissions.tsv"
local EXPLICIT_PLAN_TSV = os.getenv("CAPR_IV_EXPLICIT_PLAN_TSV") or "Germanic/docs/book/index_verborum_book_explicit_plan.tsv"

local function parse_require_completeness()
  local raw = os.getenv("CAPR_IV_REQUIRE_EXPLICIT_COMPLETENESS")
  if raw == nil or raw == "" or raw == "0" then
    return false
  end
  if raw == "1" then
    return true
  end
  error(
    "index_verborum_filter.lua: unsupported CAPR_IV_REQUIRE_EXPLICIT_COMPLETENESS '"
    .. raw .. "' (allowed: 0 or 1)"
  )
end

local REQUIRE_COMPLETENESS = parse_require_completeness()
-- ── Emission plan (for .iv-anchor path) ───────────────────────────────────────
-- emission_plan[emission_id] = precomputed_index_command
-- Loaded lazily when the first .iv-anchor span or div is encountered.
local emission_plan = nil        -- emission_id → index_command
local occurrence_to_emission = nil  -- occurrence_id → emission_id
local explicit_plan = nil -- occurrence_id -> explicit plan row
local book_explicit_emissions = nil  -- representative_occurrence_id → emission row (explicit_tag only)
local explicit_plan_ordered_ids = {}  -- ordered list of occurrence_ids (set during plan loading)
local seen_explicit_occurrence_ids = {}   -- reset per document
local seen_explicit_occurrence_order = {}  -- ordered list, reset per document
local ensure_explicit_plan_loaded

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


local function has_class(el, class_name)
  for _, class in ipairs(el.classes) do
    if class == class_name then
      return true
    end
  end
  return false
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

local function explicit_span_semantics(span)
  local lang = trim(span.attributes["lang"] or "")
  local role = trim(span.attributes["role"] or "")
  if role == "" then role = "evidence_form" end
  local source_ref = trim(span.attributes["source_ref"] or "")
  local occ_id = trim(span.attributes["occ_id"] or "")
  local variety = trim(span.attributes["variety"] or "")
  local form = normalize_iv_match_text(trim(pandoc.utils.stringify(span.content)))
  local display_attr = normalize_iv_match_text(trim(span.attributes["display"] or ""))
  local is_recon = has_class(span, "recon")
  local display = display_attr ~= "" and display_attr or (is_recon and ("*" .. form) or form)
  display = display:gsub("(%*[^%s`|<>]-%-?)%*$", "%1"):gsub("(%*[^%s`|<>]-%-?)%*([`_%.,%s;:!?)/%]%}>~])", "%1%2")
  local sort = trim(span.attributes["sort"] or form)
  return {
    lang = lang,
    role = role,
    source_ref = source_ref,
    occurrence_id = occ_id,
    variety = variety,
    form = form,
    display = display,
    sort = sort,
  }
end

local function plan_explicit_decision(sem)
  if sem.occurrence_id == "" then
    error("index_verborum_filter.lua: explicit plan mode requires nonblank occ_id (source_ref='" .. sem.source_ref .. "')")
  end
  local plan = ensure_explicit_plan_loaded()
  local row = plan[sem.occurrence_id]
  if not row then
    error("index_verborum_filter.lua: explicit occurrence_id '" .. sem.occurrence_id
      .. "' not found in explicit plan (" .. EXPLICIT_PLAN_TSV .. ")")
  end
  if row.language ~= sem.lang or row.variety ~= sem.variety
      or row.form ~= sem.form or row.display ~= sem.display
      or row.sort_key ~= sem.sort or row.form_role ~= sem.role
      or row.source_ref ~= sem.source_ref then
    error("index_verborum_filter.lua: explicit plan semantic mismatch for occ_id '"
      .. sem.occurrence_id .. "' source_ref='" .. sem.source_ref .. "'")
  end
  return {
    disposition = row.disposition,
    index_command = row.index_command,
    occurrence_id = sem.occurrence_id,
    source_ref = sem.source_ref,
    emission_id = row.emission_id,
    exclusion_reason = row.exclusion_reason,
  }
end

local function render_explicit_decision(visible, decision)
  if decision.disposition == "suppress" then
    return visible
  end
  return { visible, pandoc.RawInline("latex", decision.index_command) }
end

local function span_to_index(span)
  if not has_class(span, "iv") then
    return span
  end
  local visible = visible_span(span)
  local sem = explicit_span_semantics(span)
  local plan_decision = plan_explicit_decision(sem)
  -- Track this occurrence for per-document completeness checking.
  if seen_explicit_occurrence_ids[sem.occurrence_id] then
    error("index_verborum_filter.lua: duplicate explicit occurrence_id '"
      .. sem.occurrence_id .. "' encountered in this document")
  end
  seen_explicit_occurrence_ids[sem.occurrence_id] = true
  table.insert(seen_explicit_occurrence_order, sem.occurrence_id)
  return render_explicit_decision(visible, plan_decision)
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

    -- Store validated entry as a complete record (not just the command).
    -- This lets the anchor handler retain full context for diagnostics and
    -- future extensions, while still emitting only the precomputed command.
    emission_plan[emission_id] = {
      index_command = index_command,
      emission_path = epath,
      representative_occurrence_id = rep_occ_id,
      source_occurrence_ids = occ_ids,
    }
    for _, oid in ipairs(occ_ids) do
      occurrence_to_emission[oid] = emission_id
    end

    ::continue::
  end
  handle:close()
  return emission_plan
end

local function ensure_book_explicit_emissions_loaded()
  if book_explicit_emissions ~= nil then return book_explicit_emissions end
  book_explicit_emissions = {}
  local handle = io.open(BOOK_EMISSIONS_TSV, "r")
  if not handle then
    error("index_verborum_filter.lua: cannot read " .. BOOK_EMISSIONS_TSV
          .. " for explicit plan cross-validation.")
  end
  local header_line = handle:read("*l")
  if not header_line then
    handle:close()
    error("index_verborum_filter.lua: " .. BOOK_EMISSIONS_TSV .. " is empty (no header).")
  end
  local headers = split_tsv(header_line)
  local idx = {}
  for i, h in ipairs(headers) do idx[trim(h)] = i end
  local required = {
    "emission_id", "representative_occurrence_id", "emission_path", "index_command",
    "language", "variety", "display", "sort_key", "form_role", "source_ref",
    "source_occurrence_count", "source_occurrence_ids",
  }
  for _, col in ipairs(required) do
    if not idx[col] then
      handle:close()
      error("index_verborum_filter.lua: " .. BOOK_EMISSIONS_TSV
            .. " missing required column '" .. col .. "' for explicit plan cross-validation.")
    end
  end
  for line in handle:lines() do
    if line ~= "" then
      local cells = split_tsv(line)
      local epath = column(cells, idx["emission_path"])
      if epath == "explicit_tag" then
        local rep = column(cells, idx["representative_occurrence_id"])
        if rep ~= "" then
          book_explicit_emissions[rep] = {
            emission_id            = column(cells, idx["emission_id"]),
            emission_path          = epath,
            representative_occurrence_id = rep,
            index_command          = column(cells, idx["index_command"]),
            language               = normalize_iv_match_text(column(cells, idx["language"])),
            variety                = column(cells, idx["variety"]),
            display                = normalize_iv_match_text(column(cells, idx["display"])),
            sort_key               = column(cells, idx["sort_key"]),
            form_role              = column(cells, idx["form_role"]),
            source_ref             = column(cells, idx["source_ref"]),
            source_occurrence_count = column(cells, idx["source_occurrence_count"]),
            source_occurrence_ids  = column(cells, idx["source_occurrence_ids"]),
          }
        end
      end
    end
  end
  handle:close()
  return book_explicit_emissions
end

ensure_explicit_plan_loaded = function()
  if explicit_plan ~= nil then
    return explicit_plan
  end
  explicit_plan = {}
  local handle = io.open(EXPLICIT_PLAN_TSV, "r")
  if not handle then
    error("index_verborum_filter.lua: cannot read " .. EXPLICIT_PLAN_TSV
          .. "; run build_index_verborum.py first.")
  end
  local header_line = handle:read("*l")
  if not header_line then
    handle:close()
    error("index_verborum_filter.lua: " .. EXPLICIT_PLAN_TSV .. " is empty (no header).")
  end
  local headers = split_tsv(header_line)
  local idx = {}
  for i, h in ipairs(headers) do idx[trim(h)] = i end
  local required = {
    "occurrence_id", "disposition", "emission_id", "index_command", "exclusion_reason",
    "language", "variety", "form", "display", "sort_key", "form_role", "source_scope", "source_ref",
  }
  for _, col in ipairs(required) do
    if not idx[col] then
      handle:close()
      error("index_verborum_filter.lua: " .. EXPLICIT_PLAN_TSV
            .. " missing required column '" .. col .. "'")
    end
  end
  local row_num = 1
  local emit_emission_ids = {}
  for line in handle:lines() do
    row_num = row_num + 1
    if line == "" then goto continue end
    local cells = split_tsv(line)
    local occ_id = column(cells, idx["occurrence_id"])
    local disposition = column(cells, idx["disposition"])
    local emission_id = column(cells, idx["emission_id"])
    local index_command = column(cells, idx["index_command"])
    local exclusion_reason = column(cells, idx["exclusion_reason"])
    local language = column(cells, idx["language"])
    local variety = column(cells, idx["variety"])
    local form = normalize_iv_match_text(column(cells, idx["form"]))
    local display = normalize_iv_match_text(column(cells, idx["display"]))
    local sort_key = column(cells, idx["sort_key"])
    local form_role = column(cells, idx["form_role"])
    local source_scope = column(cells, idx["source_scope"])
    local source_ref = column(cells, idx["source_ref"])

    if occ_id == "" then
      handle:close()
      error("index_verborum_filter.lua: explicit plan row " .. row_num .. " has blank occurrence_id")
    end
    if explicit_plan[occ_id] then
      handle:close()
      error("index_verborum_filter.lua: explicit plan duplicate occurrence_id '" .. occ_id .. "'")
    end
    if disposition == "" then
      handle:close()
      error("index_verborum_filter.lua: explicit plan occurrence '" .. occ_id .. "' has blank disposition")
    end
    if disposition ~= "emit" and disposition ~= "suppress" then
      handle:close()
      error("index_verborum_filter.lua: explicit plan occurrence '" .. occ_id
            .. "' has unsupported disposition '" .. disposition .. "'")
    end
    if source_scope ~= "explicit_tag" then
      handle:close()
      error("index_verborum_filter.lua: explicit plan occurrence '" .. occ_id
            .. "' has source_scope '" .. source_scope .. "' (expected explicit_tag)")
    end
    if language == "" or form == "" or display == "" or sort_key == "" or form_role == "" or source_ref == "" then
      handle:close()
      error("index_verborum_filter.lua: explicit plan occurrence '" .. occ_id
            .. "' has blank semantic identity field")
    end

    if disposition == "emit" then
      if emission_id == "" then
        handle:close()
        error("index_verborum_filter.lua: explicit plan emit occurrence '" .. occ_id .. "' has blank emission_id")
      end
      if emission_id ~= occ_id then
        handle:close()
        error("index_verborum_filter.lua: explicit plan emit occurrence '" .. occ_id
              .. "' has emission_id '" .. emission_id .. "' (expected occurrence_id)")
      end
      if emit_emission_ids[emission_id] then
        handle:close()
        error("index_verborum_filter.lua: explicit plan duplicate emit emission_id '" .. emission_id .. "'")
      end
      emit_emission_ids[emission_id] = true
      if index_command == "" then
        handle:close()
        error("index_verborum_filter.lua: explicit plan emit occurrence '" .. occ_id .. "' has blank index_command")
      end
      if exclusion_reason ~= "" then
        handle:close()
        error("index_verborum_filter.lua: explicit plan emit occurrence '" .. occ_id .. "' has nonblank exclusion_reason")
      end
    else
      if emission_id ~= "" then
        handle:close()
        error("index_verborum_filter.lua: explicit plan suppress occurrence '" .. occ_id .. "' has nonblank emission_id")
      end
      if index_command ~= "" then
        handle:close()
        error("index_verborum_filter.lua: explicit plan suppress occurrence '" .. occ_id .. "' has nonblank index_command")
      end
      if exclusion_reason == "" then
        handle:close()
        error("index_verborum_filter.lua: explicit plan suppress occurrence '" .. occ_id .. "' has blank exclusion_reason")
      end
    end

    explicit_plan[occ_id] = {
      occurrence_id = occ_id,
      disposition = disposition,
      emission_id = emission_id,
      index_command = index_command,
      exclusion_reason = exclusion_reason,
      language = language,
      variety = variety,
      form = form,
      display = display,
      sort_key = sort_key,
      form_role = form_role,
      source_scope = source_scope,
      source_ref = source_ref,
    }

    -- ── Cross-validate against book_explicit_emissions ─────────────────────
    local bx = ensure_book_explicit_emissions_loaded()
    if disposition == "emit" then
      local bem = bx[occ_id]
      if not bem then
        handle:close()
        error("index_verborum_filter.lua: explicit plan emit occurrence '" .. occ_id
              .. "' not found in book_explicit_emissions (emission_path=explicit_tag)")
      end
      if bem.emission_path ~= "explicit_tag" then
        handle:close()
        error("index_verborum_filter.lua: explicit plan emit occurrence '" .. occ_id
              .. "' book_explicit_emissions entry has emission_path='" .. bem.emission_path .. "'")
      end
      if bem.representative_occurrence_id ~= occ_id then
        handle:close()
        error("index_verborum_filter.lua: explicit plan emit occurrence '" .. occ_id
              .. "' book_explicit_emissions representative_occurrence_id mismatch")
      end
      if bem.source_occurrence_count ~= "1" then
        handle:close()
        error("index_verborum_filter.lua: explicit plan emit occurrence '" .. occ_id
              .. "' book_explicit_emissions source_occurrence_count != '1'")
      end
      if bem.source_occurrence_ids ~= occ_id then
        handle:close()
        error("index_verborum_filter.lua: explicit plan emit occurrence '" .. occ_id
              .. "' book_explicit_emissions source_occurrence_ids mismatch")
      end
      if bem.index_command ~= index_command then
        handle:close()
        error("index_verborum_filter.lua: explicit plan emit occurrence '" .. occ_id
              .. "' index_command mismatch vs book_explicit_emissions")
      end
      for _, fld in ipairs({"language", "variety", "display", "sort_key", "form_role", "source_ref"}) do
        local plan_val = explicit_plan[occ_id][fld] or ""
        local em_val = bem[fld] or ""
        if plan_val ~= em_val then
          handle:close()
          error("index_verborum_filter.lua: explicit plan emit occurrence '" .. occ_id
                .. "' field '" .. fld .. "' mismatch vs book_explicit_emissions"
                .. " plan='" .. plan_val .. "' emissions='" .. em_val .. "'")
        end
      end
    else
      -- suppress: occurrence must NOT have an explicit_tag emission
      if bx[occ_id] then
        handle:close()
        error("index_verborum_filter.lua: explicit plan suppress occurrence '" .. occ_id
              .. "' unexpectedly found in book_explicit_emissions")
      end
    end

    -- Track loading order for document completeness check
    table.insert(explicit_plan_ordered_ids, occ_id)

    ::continue::
  end
  handle:close()
  return explicit_plan
end

-- ── .iv-anchor handler ────────────────────────────────────────────────────────
-- An .iv-anchor is a generated planned-emission anchor marker. It is not
-- hand-authored scholarly markup; it carries only emission_id, which the
-- Lua filter resolves against the precomputed emission plan.
--
-- Supported Pandoc forms:
--
--   Block:  ::: {.iv-anchor emission_id="emit:xxx"}
--           :::
--
--   Inline: []{.iv-anchor emission_id="emit:xxx"}
--
-- STRICT CONTRACT:
--   * Only emission_id belongs on the marker. No semantic fields.
--   * The anchor must be genuinely empty: no inline content (span), no blocks (div).
--   * The emission_path in the plan must not be explicit_tag.
--   * Each emission_id may fire at most once per Pandoc document.
--   * The marker class must not co-occur with .iv, .recon, .pred, .lex, or .ex.
--   * Block anchors emit a pandoc.RawBlock; inline anchors emit pandoc.RawInline.
--   * No visible content is produced in any output format.
--   * The index_command is stored verbatim and emitted without any modification.
--
-- Document-level duplicate tracking is reset at the start of each Pandoc run.

local emitted_anchor_ids = {}   -- reset per document

local CONTRADICTORY_ANCHOR_CLASSES = {
  iv = true, recon = true, pred = true, lex = true, ex = true,
}

local function validate_anchor_class_or_fail(classes, context)
  for _, cls in ipairs(classes) do
    if CONTRADICTORY_ANCHOR_CLASSES[cls] then
      error("index_verborum_filter.lua: .iv-anchor " .. context
            .. " has contradictory class '." .. cls
            .. "' — anchors must not co-occur with semantic span classes")
    end
  end
end

local function anchor_emit(emission_id, context)
  -- 1. Blank emission_id
  if emission_id == nil or emission_id == "" then
    error("index_verborum_filter.lua: .iv-anchor " .. context
          .. " has blank or missing emission_id")
  end

  -- 2. Load plan
  local plan = ensure_emission_plan_loaded()
  local record = plan[emission_id]

  -- 3. Unknown emission_id
  if record == nil then
    error("index_verborum_filter.lua: .iv-anchor " .. context
          .. " emission_id '" .. emission_id
          .. "' not found in emission plan (" .. BOOK_EMISSIONS_TSV .. ")")
  end

  -- 4. Explicit-tag emission must not be anchored
  if record.emission_path == "explicit_tag" then
    error("index_verborum_filter.lua: .iv-anchor " .. context
          .. " emission_id '" .. emission_id
          .. "' has emission_path=explicit_tag — explicit spans must use .iv, not .iv-anchor")
  end

  -- 5. Duplicate anchor in this document
  if emitted_anchor_ids[emission_id] then
    error("index_verborum_filter.lua: .iv-anchor " .. context
          .. " emission_id '" .. emission_id
          .. "' has already been anchored in this document (duplicate anchor)")
  end
  emitted_anchor_ids[emission_id] = true

  -- Emit the exact precomputed command. Lua never reconstructs index_command.
  return record.index_command
end

local function span_is_anchor(span)
  for _, cls in ipairs(span.classes) do
    if cls == "iv-anchor" then return true end
  end
  return false
end

local function handle_anchor_span(span)
  if not span_is_anchor(span) then return nil end

  -- Class contradictions
  validate_anchor_class_or_fail(span.classes, "inline span")

  -- Inline anchor must have no content (genuinely empty)
  if #span.content > 0 then
    error("index_verborum_filter.lua: .iv-anchor inline span with emission_id '"
          .. (span.attributes["emission_id"] or "")
          .. "' has non-empty inline content — anchors must be empty: []{.iv-anchor ...}")
  end

  local emission_id = trim(span.attributes["emission_id"] or "")
  local cmd = anchor_emit(emission_id, "inline span")
  return { pandoc.RawInline("latex", cmd) }
end

local function div_is_anchor(div)
  for _, cls in ipairs(div.classes) do
    if cls == "iv-anchor" then return true end
  end
  return false
end

local function handle_anchor_div(div)
  if not div_is_anchor(div) then return nil end

  -- Class contradictions
  validate_anchor_class_or_fail(div.classes, "block div")

  -- Block anchor must have no content blocks
  if #div.content > 0 then
    error("index_verborum_filter.lua: .iv-anchor block div with emission_id '"
          .. (div.attributes["emission_id"] or "")
          .. "' has non-empty block content — anchors must be empty: ::: {.iv-anchor ...}\\n:::")
  end

  local emission_id = trim(div.attributes["emission_id"] or "")
  local cmd = anchor_emit(emission_id, "block div")
  -- Block anchor emits a raw block (not a Plain paragraph) so it disappears
  -- from non-LaTeX output without leaving a blank paragraph.
  return pandoc.RawBlock("latex", cmd)
end

function Pandoc(doc)
  -- Reset per-document tracking.
  emitted_anchor_ids = {}
  seen_explicit_occurrence_ids = {}
  seen_explicit_occurrence_order = {}
  local blocks = {}
  for _, block in ipairs(doc.blocks) do
    if block.t == "Div" and block.identifier == "refs" then
      table.insert(blocks, block)
    elseif block.t == "Div" and div_is_anchor(block) then
      -- Block-level .iv-anchor: emit precomputed command via RawBlock.
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
  -- ── Explicit plan completeness check ─────────────────────────────────────
  if REQUIRE_COMPLETENESS then
    ensure_explicit_plan_loaded()
    local plan_n = #explicit_plan_ordered_ids
    local seen_n = #seen_explicit_occurrence_order
    if seen_n ~= plan_n then
      error("index_verborum_filter.lua: explicit plan completeness failure: "
            .. "plan has " .. plan_n .. " occurrences but document contained " .. seen_n)
    end
    for i = 1, plan_n do
      local expected = explicit_plan_ordered_ids[i]
      local actual = seen_explicit_occurrence_order[i]
      if expected ~= actual then
        error("index_verborum_filter.lua: explicit plan completeness failure at position " .. i
              .. ": expected='" .. (expected or "") .. "' actual='" .. (actual or "") .. "'")
      end
    end
  end
  return pandoc.Pandoc(blocks, doc.meta)
end
