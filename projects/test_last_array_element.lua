local wf = require("wf")
local emails = wf.vars.emails
local last_email = table.remove(emails, #emails)
print(last_email)