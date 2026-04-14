# luaL_checklstring

**Category**: Auxiliary Library

### `luaL_checklstring`[-0, +0, *v*]

```lua
const char *luaL_checklstring (lua_State *L, int arg, size_t *l);
```

Checks whether the function argument `arg` is a string and returns this string; if `l` is not `NULL` fills its referent with the string's length.

This function uses [`lua_tolstring`](#lua_tolstring) to get its result, so all conversions and caveats of that function apply here.