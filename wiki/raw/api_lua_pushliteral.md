# lua_pushliteral

**Category**: API

### `lua_pushliteral`[-0, +1, *v*]

```lua
const char *lua_pushliteral (lua_State *L, const char *s);
```

This macro is equivalent to [`lua_pushstring`](#lua_pushstring), but should be used only when `s` is a literal string. (Lua may optimize this case.)