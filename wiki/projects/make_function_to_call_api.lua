function api_request(url)
    local http = require('lua_http')
    return http:call_request(http.state, 'POST', url)
end