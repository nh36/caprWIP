-- lex_form_filter.lua
-- Rendering filter for .lex semantic markup.
--
-- .lex marks an ordinary lexical linguistic form that does not require
-- Index verborum membership. It has no index side effects.
-- Rendering: plain italic of the span's text content, identical to how
-- an ordinary italicised form would appear.
--
-- This is a render-only filter; validation is handled by paragraph_gloss_validator.lua.

local pandoc = require 'pandoc'

function Span(span)
  local classes = span.classes
  if not classes then return nil end
  for _, c in ipairs(classes) do
    if c == 'lex' then
      -- Render as plain italic
      return pandoc.Emph(span.content)
    end
    if c == 'ex' then
      -- .ex (example phrase) renders as plain italic too, but no semantic checking
      return pandoc.Emph(span.content)
    end
  end
  return nil
end
