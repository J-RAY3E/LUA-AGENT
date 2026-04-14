# luaL_checkinteger

**Category**: Auxiliary Library

### `luaL_checkinteger`[-0, +0, *v*]

```lua
lua_Integer luaL_checkinteger (lua_State *L, int arg);
```

Checks whether the function argument `arg` is an integer (or can be converted to an integer) and returns this integer.