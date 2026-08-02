local PRINT_MAIN_TSV = os.getenv("CAPR_IV_PRINT_MAIN_TSV") or "Germanic/docs/book/index_verborum_print_main.tsv"
local EXPLICIT_ALLOW_SORTKEY_TSV = os.getenv("CAPR_IV_EXPLICIT_ALLOW_SORTKEY_TSV") or "Germanic/docs/book/index_verborum_explicit_allow_sortkey.tsv"
local LANGUAGE_REGISTRY_TSV = os.getenv("CAPR_IV_LANGUAGE_REGISTRY_TSV") or "Germanic/docs/book/index_verborum_languages.tsv"
local VARIETY_REGISTRY_TSV = os.getenv("CAPR_IV_VARIETY_REGISTRY_TSV") or "Germanic/docs/book/index_verborum_varieties.tsv"
local lang_meta = nil  -- {code → {order_str, title, escaped_title}}
local variety_meta = nil  -- {code → {printed_label, display_order, assignable, active, language, suppress}}
local explicit_allow = nil
local explicit_allow_sortkey = nil  -- sort-key-based allowlist (bypasses Unicode normalization)

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
        local form = column(cells, indices["form"])
        local display = column(cells, indices["display"])
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
    if key ~= "lang" and key ~= "sort" and key ~= "display" and key ~= "source_scope" and key ~= "source_ref" and key ~= "role" and key ~= "variety" then
      filtered_attrs[key] = value
    end
  end
  local content = span.content
  if trim(span.attributes["lang"] or "") == "oe" then
    content = italicize_oe_content(content)
  end
  return pandoc.Span(content, pandoc.Attr(span.identifier, filtered_classes, filtered_attrs))
end

local function ensure_sortkey_allow_loaded()
  if explicit_allow_sortkey ~= nil then
    return explicit_allow_sortkey
  end
  explicit_allow_sortkey = {}
  local handle = io.open(EXPLICIT_ALLOW_SORTKEY_TSV, "r")
  if not handle then
    -- File may not exist in older checkouts; fall back to form-based matching only.
    explicit_allow_sortkey = {}
    return explicit_allow_sortkey
  end
  local header_line = handle:read("*l")
  if not header_line then
    handle:close()
    explicit_allow_sortkey = {}
    return explicit_allow_sortkey
  end
  local headers = split_tsv(header_line)
  local indices = {}
  for i, name in ipairs(headers) do indices[name] = i end
  for line in handle:lines() do
    if line ~= "" then
      local cells = split_tsv(line)
      local language = column(cells, indices["language"])
      local role = column(cells, indices["form_role"])
      local sort_key = column(cells, indices["sort_key"])
      -- The allowlist now uses occurrence_id (unique per span) for disambiguation.
      -- Fall back to source_ref for older allowlist files without the column.
      local occ_id = column(cells, indices["occurrence_id"]) ~= "" and column(cells, indices["occurrence_id"])
                     or column(cells, indices["source_ref"])
      local variety = column(cells, indices["variety"])
      explicit_allow_sortkey[explicit_key(language, role, sort_key, occ_id, variety)] = true
    end
  end
  handle:close()
  return explicit_allow_sortkey
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
  -- Primary check: form/display-based (may fail for NFC vs NFD Unicode mismatch)
  if allow[explicit_key(language, role, form, source_ref, variety)]
      or allow[explicit_key(language, role, display, source_ref, variety)] then
    return true
  end
  -- Fallback: sort-key-based allowlist (always ASCII, normalization-immune).
  -- Used when Pandoc stringifies a span to NFD but the TSV stores NFC.
  return false  -- sort-key check is done at call site where sort is available
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
  local form = trim(pandoc.utils.stringify(span.content))
  local display_attr = trim(span.attributes["display"] or "")
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
  -- Check printability: primary form/display check, then sort-key fallback to
  -- handle Pandoc NFD vs TSV NFC normalization mismatches.
  local printable = explicit_tag_is_printable(lang, role, form, display, source_ref, variety)
  if not printable then
    local sortkey_allow = ensure_sortkey_allow_loaded()
    -- Use occ_id for the fallback when available (handles same-line duplicates);
    -- fall back to source_ref for spans without occ_id.
    local ref_for_fallback = occ_id ~= "" and occ_id or source_ref
    printable = sortkey_allow[explicit_key(lang, role, sort, ref_for_fallback, variety)] or false
  end
  if not printable then
    return visible
  end
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

function Pandoc(doc)
  local blocks = {}
  for _, block in ipairs(doc.blocks) do
    if block.t == "Div" and block.identifier == "refs" then
      table.insert(blocks, block)
    else
      table.insert(blocks, block:walk({ Span = span_to_index }))
    end
  end
  return pandoc.Pandoc(blocks, doc.meta)
end
