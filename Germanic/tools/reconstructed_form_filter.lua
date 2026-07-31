-- reconstructed_form_filter.lua
-- Rendering-only Pandoc Lua filter: maps Span with class 'recon' to raw LaTeX \Recon{...}
-- The \Recon macro supplies the reconstruction asterisk itself; do not include a
-- leading '*' in the span content.
--
-- Source:  [júką]{.recon}
-- Output:  \Recon{júką}
-- Rendered: *júką  (italic, asterisk supplied by the macro)
--
-- A span content beginning with '*' or '\*' is a hard error: it would produce '**form'
-- in the PDF because \Recon already prepends the asterisk.
function Span(el)
  if el.classes:includes('recon') then
    local inner = pandoc.utils.stringify(el)
    -- Fail hard if the content starts with a literal or escaped asterisk.
    -- This produces **form in the PDF since \Recon{} supplies the first *.
    if inner:match("^%*") or inner:match("^\\%*") then
      error(
        "reconstructed_form_filter.lua: malformed .recon span — span content must not begin with '*'.\n"
        .. "\\Recon{} supplies the reconstruction asterisk; a leading * in the content produces **form.\n"
        .. "Fix: use [" .. inner:gsub("^\\?%*", "") .. "]{.recon} without the leading asterisk.\n"
        .. "Malformed content: '" .. inner .. "'"
      )
    end
    return pandoc.RawInline('latex', '\\Recon{' .. inner .. '}')
  end
  return nil
end
