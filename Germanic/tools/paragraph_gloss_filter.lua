-- paragraph_gloss_filter.lua
-- Inserts English glosses after first Emph per paragraph using manifest_all_by_class.tsv
local pandoc = require 'pandoc'
local utils = pandoc.utils

local manifest_path = 'Germanic/docs/assembly/manifest_all_by_class.tsv'
local manifest = {}

-- load manifest into table mapping normalized form -> gloss
local function load_manifest()
  local f = io.open(manifest_path, 'r')
  if not f then return end
  local header = f:read('*l')
  for line in f:lines() do
    local parts = {}
    for part in string.gmatch(line, '([^	]*)	?') do
      table.insert(parts, part)
    end
    local lexical_item = parts[4] or ''
    local key = string.lower(lexical_item:gsub('[^a-z]', ''))
    if key ~= '' then
      manifest[key] = lexical_item
    end
  end
  f:close()
end

load_manifest()

local function normalize(s)
  return (string.lower(s):gsub('[^a-z]', ''))
end

function Para(el)
  local seen = {}
  local out = {}
  local i = 1
  while i <= #el.content do
    local inline = el.content[i]
    if inline.t == 'Emph' then
      local form = utils.stringify(inline)
      if not seen[form] then
        seen[form] = true
        -- check next non-space inline for quote or gloss
        local j = i + 1
        while j <= #el.content and el.content[j].t == 'Space' do j = j + 1 end
        local has_gloss = false
        if j <= #el.content then
          local nxt = el.content[j]
          if nxt.t == 'Str' then
            if string.match(nxt.text, "^[‘'\"]") then has_gloss = true end
          elseif nxt.t == 'Quoted' then
            has_gloss = true
          end
        end
        if not has_gloss then
          local key = normalize(form)
          local gloss = manifest[key]
          if gloss then
            -- insert Str containing space and quoted gloss
            table.insert(out, inline)
            table.insert(out, pandoc.Space())
            table.insert(out, pandoc.Str("'" .. gloss .. "'"))
            i = i + 1
            goto continue
          end
        end
      end
    end
    table.insert(out, inline)
    ::continue::
    i = i + 1
  end
  if #out > 0 then
    el.content = out
    return el
  end
  return nil
end
