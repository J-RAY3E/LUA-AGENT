local data = wf.initVariables.recallTime
local parsedData = string.unpack("a8", data)
local unixTime = parsedData
return unixTime