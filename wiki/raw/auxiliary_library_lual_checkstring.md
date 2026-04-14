# luaL_checkstring

**Category**: Auxiliary Library

### `luaL_checkstring`[-0, +0, *v*]

```lua
const char *luaL_checkstring (lua_State *L, int arg);
```

Checks whether the function argument `arg` is a string and returns this string.

This function uses [`lua_tolstring`](#lua_tolstring) to get its result, so all conversions and caveats of that function apply here.