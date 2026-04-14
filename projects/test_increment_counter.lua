local wf = require("wf")
local vars = wf.vars
local function increase_try_count_n()
    local try_count_n = vars.try_count_n
    try_count_n = try_count_n + 1
    vars.try_count_n = try_count_n
end
increase_try_count_n()
print(vars.try_count_n)