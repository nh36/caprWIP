-- predicted_marking_filter.lua
-- Marks predicted counterfactual outputs by converting Emph elements to Span with class 'pred'
local pandoc = require 'pandoc'
local stringify = pandoc.utils.stringify

local contrastors = {'rather than', 'instead of', 'instead of the expected', 'rather than expected', 'rather than the expected'}
local produces_words = {'yields', 'produces', 'would yield', 'would produce', 'would have produced'}

function contains_any(s, tbl)
  s = string.lower(s)
  for _,v in ipairs(tbl) do
    if string.find(s, v, 1, true) then return true end
  end
  return false
end

function Para(el)
  local text = stringify(el)
  local lowered = string.lower(text)
  if contains_any(lowered, contrastors) then
    -- find the position of the first contrastor
    for _, c in ipairs(contrastors) do
      local i,j = string.find(lowered, c, 1, true)
      if i then
        -- iterate inlines and convert the last Emph before i
        local last_emph_index = nil
        local char_count = 0
        for idx,inline in ipairs(el.content) do
          local s = stringify(inline)
          char_count = char_count + #s
          if inline.t == 'Emph' then
            -- record index; may be overwritten so last Emph before connector wins
            if char_count < i then
              last_emph_index = idx
            end
          end
        end
        if last_emph_index then
          local emph = el.content[last_emph_index]
          -- wrap as Span with class 'pred'
          local sp = pandoc.Span(emph.content, pandoc.Attr('', {'pred'}))
          el.content[last_emph_index] = sp
          return el
        end
      end
    end
  elseif contains_any(lowered, produces_words) and string.find(lowered, 'expected', 1, true) then
    -- mark first Emph after 'yields'
    for _, pword in ipairs(produces_words) do
      local i,j = string.find(lowered, pword, 1, true)
      if i then
        -- find first Emph after j
        local char_count = 0
        for idx,inline in ipairs(el.content) do
          local s = stringify(inline)
          if char_count >= j and inline.t == 'Emph' then
            local sp = pandoc.Span(inline.content, pandoc.Attr('', {'pred'}))
            el.content[idx] = sp
            return el
          end
          char_count = char_count + #s
        end
      end
    end
  end
  return nil
end
