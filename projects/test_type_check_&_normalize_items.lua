function ensure_items_as_array(package)
    if type(package.items) == "table" and not package.items[1] then
        package.items = {
            package.items,
        }
    end
end
function process_packages(packages)
    for _, package in ipairs(packages) do
        ensure_items_as_array(package)
    end
end
local function transform_data(data)
    local packages = data.wf.vars.json.IDOC.ZCDF_HEAD.ZCDF_PACKAGES
    process_packages(packages)
    return data
end
return transform_data