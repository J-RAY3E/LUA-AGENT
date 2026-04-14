local function filterItems(items)
    local filtered = {
    }
    for _, item in ipairs(items) do
        if item.Discount ~= "" and item.Markdown ~= "" then
            table.insert(filtered, item)
        end
    end
    return filtered
end
return filterItems(wf.vars.parsedCsv)