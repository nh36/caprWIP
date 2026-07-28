-- Pandoc Lua filter: map span with class 'pred' to raw LaTeX \Pred{...}
function Span(el)
  if el.classes:includes('pred') then
    -- render content as inner text
    local inner = pandoc.utils.stringify(el)
    -- produce RawInline LaTeX
    return pandoc.RawInline('latex', '\\Pred{' .. inner .. '}')
  end
  return nil
end
