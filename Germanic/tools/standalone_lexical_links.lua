-- Companion rule references have destinations only in the combined book.
function Pandoc(doc)
  local destinations = {}
  local function collect(el)
    if el.identifier and el.identifier ~= "" then
      destinations[el.identifier] = true
    end
  end
  doc:walk({
    Header = collect, Div = collect, Span = collect, Code = collect,
    CodeBlock = collect, Table = collect, Figure = collect,
    Link = collect, Image = collect
  })
  return doc:walk({
    Link = function(el)
      local target = el.target:match("^#(rule%-.+)$")
      if target and not destinations[target] then
        return el.content
      end
    end
  })
end
