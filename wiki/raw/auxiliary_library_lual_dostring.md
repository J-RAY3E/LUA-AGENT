# luaL_dostring

**Category**: Auxiliary Library

### `luaL_dostring`[-0, +?, –]

```lua
int luaL_dostring (lua_State *L, const char *str);
```

Loads and runs the given string. It is defined as the following macro:

```lua
(luaL_loadstring(L, str) || lua_pcall(L, 0, LUA_MULTRET, 0))
```

It returns 0 ([`LUA_OK`](#pdf-LUA_OK)) if there are no errors, or 1 in case of errors.