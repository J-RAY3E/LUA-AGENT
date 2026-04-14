function loop()
    local str = luas
    Pushliteral("Hello")
    local str2 = luas
    Pushliteral(" World")
    local s = luas
    Tolerancestring(1, 0)
    s = s:Convert(s, "string")
    return str + " " + s
end
return loop()