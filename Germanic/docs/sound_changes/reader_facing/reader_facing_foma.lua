function CodeBlock(el)
  if not FORMAT:match("latex") then
    return nil
  end
  for _, class in ipairs(el.classes) do
    if class == "foma" then
      local lines, longest = 0, 0
      for line in (el.text .. "\n"):gmatch("(.-)\n") do
        lines = lines + 1
        longest = math.max(longest, utf8.len(line))
      end
      local block = "\\begin{ReaderFacingFoma}\n" .. el.text .. "\n\\end{ReaderFacingFoma}"
      if lines <= 8 and longest <= 80 then
        block = "\\noindent\\begin{minipage}{\\linewidth}\n" .. block ..
          "\n\\end{minipage}"
      end
      return pandoc.RawBlock("latex", block)
    end
  end
  return nil
end
