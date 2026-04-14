# Pointers to Strings

**Category**: API

### 4.1.3 – Pointers to Strings

Several functions in the API return pointers (`const char*`) to Lua strings in the stack. (See [`lua_pushfstring`](#lua_pushfstring), [`lua_pushlstring`](#lua_pushlstring), [`lua_pushstring`](#lua_pushstring), and [`lua_tolstring`](#lua_tolstring). See also [`luaL_checklstring`](#luaL_checklstring), [`luaL_checkstring`](#luaL_checkstring), and [`luaL_tolstring`](#luaL_tolstring) in the auxiliary library.)

In general, Lua's garbage collection can free or move memory and then invalidate pointers to strings handled by a Lua state. To allow a safe use of these pointers, the API guarantees that any pointer to a string in a stack index is valid while the string value at that index is not removed from the stack. (It can be moved to another index, though.) When the index is a pseudo-index (referring to an upvalue), the pointer is valid while the corresponding call is active and the corresponding upvalue is not modified.

Some functions in the debug interface also return pointers to strings, namely [`lua_getlocal`](#lua_getlocal), [`lua_getupvalue`](#lua_getupvalue), [`lua_setlocal`](#lua_setlocal), and [`lua_setupvalue`](#lua_setupvalue). For these functions, the pointer is guaranteed to be valid while the caller function is active and the given closure (if one was given) is in the stack.

Except for these guarantees, the garbage collector is free to invalidate any pointer to internal strings.