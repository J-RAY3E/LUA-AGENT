# luaL_optinteger

**Category**: Auxiliary Library

### `luaL_optinteger`[-0, +0, *v*]

```lua
lua_Integer luaL_optinteger (lua_State *L,
                             int arg,
                             lua_Integer d);
```

If the function argument `arg` is an integer (or it is convertible to an integer), returns this integer. If this argument is absent or is **nil**, returns `d`. Otherwise, raises an error.