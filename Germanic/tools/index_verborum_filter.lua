local PRINT_MAIN_TSV = os.getenv("CAPR_IV_PRINT_MAIN_TSV") or "Germanic/docs/book/index_verborum_print_main.tsv"
local LANGUAGE_REGISTRY_TSV = os.getenv("CAPR_IV_LANGUAGE_REGISTRY_TSV") or "Germanic/docs/book/index_verborum_languages.tsv"
local lang_meta = nil  -- {code → {order_str, title, escaped_title}}
local explicit_allow = nil

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

local function explicit_key(language, role, value, source_ref)
  return (language or "") .. "\t" .. (role or "") .. "\t" .. (value or "") .. "\t" .. (source_ref or "")
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
  local code_idx, title_idx, active_idx = nil, nil, nil
  for i, h in ipairs(headers) do
    if h == "code" then code_idx = i
    elseif h == "title" then title_idx = i
    elseif h == "active" then active_idx = i
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
      if code ~= "" and active == "1" then
        order = order + 1
        local order_str = string.format("%02d", order)
        -- escape @ and ! in title for MakeIndex
        local escaped = title:gsub("@", "\\@"):gsub("!", "\\!")
        lang_meta[code] = {order_str = order_str .. code, title = title, escaped_title = "\\textbf{" .. escaped .. "}"}
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
        if role == "" then
          role = "evidence_form"
        end
        explicit_allow[explicit_key(language, role, form, source_ref)] = true
        explicit_allow[explicit_key(language, role, display, source_ref)] = true
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
    if key ~= "lang" and key ~= "sort" and key ~= "display" and key ~= "source_scope" and key ~= "source_ref" and key ~= "role" then
      filtered_attrs[key] = value
    end
  end
  local content = span.content
  if trim(span.attributes["lang"] or "") == "oe" then
    content = italicize_oe_content(content)
  end
  return pandoc.Span(content, pandoc.Attr(span.identifier, filtered_classes, filtered_attrs))
end

local function explicit_tag_is_printable(language, role, form, display, source_ref)
  if language == "" then
    return false
  end
  -- Note: preoe forms are now allowed to print if they appear in print_main.
  -- The blanket preoe exclusion was removed (§11 fix); use print_main as the authority.
  local allow = ensure_print_main_loaded()
  if source_ref == "" then
    return false
  end
  return allow[explicit_key(language, role, form, source_ref)] or allow[explicit_key(language, role, display, source_ref)] or false
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
  local form = trim(pandoc.utils.stringify(span.content))
  local display = trim(span.attributes["display"] or form)
  local sort = trim(span.attributes["sort"] or display)
  if not explicit_tag_is_printable(lang, role, form, display, source_ref) then
    return visible
  end
  local index_display = latex_escape(display)
  if lang == "oe" then
    index_display = "\\emph{" .. index_display .. "}"
  end
  local meta = ensure_lang_meta_loaded()
  local lm = meta[lang]
  local lang_sort = lm and lm.order_str or ("99" .. lang)
  local lang_display = lm and lm.escaped_title or ("\\textbf{" .. lang .. "}")
  local raw = pandoc.RawInline("latex", "\\index[iv]{" .. lang_sort .. "@" .. lang_display .. "!" .. latex_escape(sort) .. "@" .. index_display .. "}")
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
