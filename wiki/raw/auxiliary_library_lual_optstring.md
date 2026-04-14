# luaL_optstring

**Category**: Auxiliary Library

### `luaL_optstring`[-0, +0, *v*]

```lua
const char *luaL_optstring (lua_State *L,
                            int arg,
                            const char *d);
```

If the function argument `arg` is a string, returns this string. If this argument is absent or is **nil**, returns `d`. Otherwise, raises an error.