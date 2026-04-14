local function convertToUnixTime(recallTime)
    local timeTable = os.date("*t", os.time({
        year = tonumber(string.sub(recallTime, 1, 4)),
        month = tonumber(string.sub(recallTime, 6, 7)),
        day = tonumber(string.sub(recallTime, 9, 10)),
        hour = tonumber(string.sub(recallTime, 12, 13)),
        min = tonumber(string.sub(recallTime, 15, 16)),
        sec = tonumber(string.sub(recallTime, 18, 19)),
    }))
    return os.time(timeTable)
end
return convertToUnixTime(wf.initVariables.recallTime)