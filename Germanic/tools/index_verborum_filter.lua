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

local function span_to_index(span)
  if not has_class(span, "iv") then
    return span
  end
  local lang = span.attributes["lang"] or ""
  if lang == "" then
    return span
  end
  local display = span.attributes["display"] or pandoc.utils.stringify(span.content)
  local sort = span.attributes["sort"] or display
  local filtered_classes = {}
  for _, class in ipairs(span.classes) do
    if class ~= "iv" then
      table.insert(filtered_classes, class)
    end
  end
  local filtered_attrs = {}
  for key, value in pairs(span.attributes) do
    if key ~= "lang" and key ~= "sort" and key ~= "display" and key ~= "source_scope" then
      filtered_attrs[key] = value
    end
  end
  local visible = pandoc.Span(span.content, pandoc.Attr(span.identifier, filtered_classes, filtered_attrs))
  local raw = pandoc.RawInline("latex", "\\index[" .. lang .. "]{" .. latex_escape(sort) .. "@" .. latex_escape(display) .. "}")
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
