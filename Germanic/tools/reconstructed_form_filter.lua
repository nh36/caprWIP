-- reconstructed_form_filter.lua
-- Rendering-only Pandoc Lua filter: maps Span with class 'recon' to raw LaTeX \Recon{...}
-- The \Recon macro supplies the reconstruction asterisk itself; do not include a
-- leading '*' in the span content.
--
-- Source:  [júką]{.recon}
-- Output:  \Recon{júką}
-- Rendered: *júką  (italic, asterisk supplied by the macro)
function Span(el)
  if el.classes:includes('recon') then
    local inner = pandoc.utils.stringify(el)
    return pandoc.RawInline('latex', '\\Recon{' .. inner .. '}')
  end
  return nil
end
