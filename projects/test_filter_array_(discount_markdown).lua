local parsedCsv = wf.vars.parsedCsv
local filteredCsv = {
}
for _, row in ipairs(parsedCsv) do
    if row.Discount ~= nil or row.Markdown ~= nil then
        table.insert(filteredCsv, row)
    end
end
return filteredCsv