local function cleanVariables(data)
    local wf = data.wf
    local vars = wf.vars.RESTbody.result
    for _, item in ipairs(vars) do
        for key, value in pairs(item) do
            if key == "ID" then
                item[key] = nil
            elseif key == "ENTITY_ID" then
                item[key] = nil
            elseif key == "CALL" then
                item[key] = nil
            end
        end
    end
end
return cleanVariables