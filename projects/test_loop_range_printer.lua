function local_sum(a, b)
    local sum
    if not table.tdict.keys(a) then
        return 0
    end
    sum = a + b
    return sum
end