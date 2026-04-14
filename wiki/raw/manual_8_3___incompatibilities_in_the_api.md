# 8.3 – Incompatibilities in the API

**Category**: Manual

## 8.3 – Incompatibilities in the API

* In [`lua_call`](#lua_call) and related functions, the maximum value for the number of required results (`nresults`) is 250. If you really need a larger value, use [`LUA_MULTRET`](#pdf-LUA_MULTRET) and then adjust the stack size. Previously, this limit was unspecified.
* [`lua_newstate`](#lua_newstate) has a third parameter, a seed for the hashing of strings.
* The function `lua_resetthread` is deprecated; it is equivalent to [`lua_closethread`](#lua_closethread) with `from` being `NULL`.
* The function `lua_setcstacklimit` is deprecated. Calls to it can simply be removed.
* The function [`lua_dump`](#lua_dump) changed the way it keeps the stack through the calls to the writer function. (That was not specified in previous versions.) Also, it calls the writer function one extra time, to signal the end of the dump.
* Parameters for the garbage collection are not set with the options [`LUA_GCINC`](#pdf-LUA_GCINC) and [`LUA_GCGEN`](#pdf-LUA_GCGEN); instead, there is a new option [`LUA_GCPARAM`](#pdf-LUA_GCPARAM) to that end. Moreover, there were some changes in the parameters themselves.
* The function [`lua_pushvfstring`](#lua_pushvfstring) now reports errors, instead of raising them.