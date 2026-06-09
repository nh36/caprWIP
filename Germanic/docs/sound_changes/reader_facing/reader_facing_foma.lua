function CodeBlock(el)
  if not FORMAT:match("latex") then
    return nil
  end
  for _, class in ipairs(el.classes) do
    if class == "foma" then
      return pandoc.RawBlock(
        "latex",
        "\\begin{ReaderFacingFoma}\n" .. el.text .. "\n\\end{ReaderFacingFoma}"
      )
    end
  end
  return nil
end
