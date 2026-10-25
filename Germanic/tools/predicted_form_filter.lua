-- Pandoc Lua filter: map span with class 'pred' to raw LaTeX \Pred{...}
function Span(el)
  if el.classes:includes('pred') then
    el.content:walk({
      RawInline = function(raw)
        error(".pred requires ordinary semantic form content, not raw " .. raw.format)
      end
    })
    local inner = pandoc.utils.stringify(el)
    if inner:match("^%s*$") then
      error(".pred form must not be empty")
    end
    if FORMAT:match("latex") then
      local escaped = pandoc.write(pandoc.Pandoc({
        pandoc.Plain({pandoc.Str(inner)})
      }), "latex"):gsub("%s+$", "")
      return pandoc.RawInline('latex', '\\Pred{' .. escaped .. '}')
    end
  end
  return nil
end
