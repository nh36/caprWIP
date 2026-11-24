local function replace_angles(element)
  local text = element.text
  local output = {}
  local open_angle = "⟨"
  local close_angle = "⟩"
  local open_latex = "\\ensuremath{\\langle}"
  local close_latex = "\\ensuremath{\\rangle}"

  while true do
    local open_at = text:find(open_angle, 1, true)
    local close_at = text:find(close_angle, 1, true)
    if not open_at and not close_at then break end

    local position = open_at and close_at and math.min(open_at, close_at)
      or open_at or close_at
    if position > 1 then
      table.insert(output, pandoc.Str(text:sub(1, position - 1)))
    end
    if position == open_at then
      table.insert(output, pandoc.RawInline("latex", open_latex))
      text = text:sub(position + #open_angle)
    else
      table.insert(output, pandoc.RawInline("latex", close_latex))
      text = text:sub(position + #close_angle)
    end
  end

  if #output == 0 then return nil end
  if #text > 0 then table.insert(output, pandoc.Str(text)) end
  return output
end

function Str(element)
  return replace_angles(element)
end
