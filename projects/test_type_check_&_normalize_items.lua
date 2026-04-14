local data = {
    wf = {
        vars = {
            json = {
                IDOC = {
                    ZCDF_HEAD = {
                        ZCDF_PACKAGES = {
                            {
                                id = "PKG001",
                                number = "EXIDV001",
                                weight = "10",
                                volume = "50",
                                length = "100",
                                width = "50",
                                height = "30",
                                items = {
                                    {
                                        sku = "SKU001",
                                        externalId = "MAT001",
                                        quantity = "5",
                                        weight = "2",
                                    },
                                    {
                                        sku = "SKU002",
                                        externalId = "MAT002",
                                        quantity = "3",
                                        weight = "1",
                                    },
                                },
                            },
                            {
                                id = "PKG002",
                                number = "EXIDV002",
                                weight = "20",
                                volume = "60",
                                length = "120",
                                width = "60",
                                height = "40",
                                items = {
                                    sku = "SKU003",
                                },
                            },
                        },
                    },
                },
            },
        },
    },
}
local function convertItemsToArray(items)
    if type(items) == "table" then
        return items
    else
        return {
            items,
        }
    end
end
for _, package in ipairs(data.wf.vars.json.IDOC.ZCDF_HEAD.ZCDF_PACKAGES) do
    for _, item in ipairs(package.items) do
        package.items = convertItemsToArray(package.items)
    end
end
print(data.wf.vars.json.IDOC.ZCDF_HEAD.ZCDF_PACKAGES)
return data