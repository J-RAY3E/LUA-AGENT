function convert_to_iso8601(date, time)
    local date_str = date .. time
    local iso8601_str = string.format("%04d%02d%02d%02d%02d%02d", tonumber(date_str:sub(1, 4)), tonumber(date_str:sub(5, 6)), tonumber(date_str:sub(7, 8)), tonumber(date_str:sub(9, 10)), tonumber(date_str:sub(11, 12)), tonumber(date_str:sub(13, 14)))
    return iso8601_str
end
local date = "20231015"
local time = "153000"
local iso8601 = convert_to_iso8601(date, time)
print(iso8601)