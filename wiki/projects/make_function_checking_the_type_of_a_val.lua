local aux = require('auxiliary')
function type_check(value)
    return aux.luaL_is(value, "true", "false", "integer", "string", "number", "boolean")
end