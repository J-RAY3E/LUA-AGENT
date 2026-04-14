# luaL_optlstring

**Category**: Auxiliary Library

### `luaL_optlstring`[-0, +0, *v*]

```lua
const char *luaL_optlstring (lua_State *L,
                             int arg,
                             const char *d,
                             size_t *l);
```

If the function argument `arg` is a string, returns this string. If this argument is absent or is **nil**, returns `d`. Otherwise, raises an error.

If `l` is not `NULL`, fills its referent with the result's length. If the result is `NULL` (only possible when returning `d` and `d == NULL`), its length is considered zero.

This function uses [`lua_tolstring`](#lua_tolstring) to get its result, so all conversions and caveats of that function apply here.