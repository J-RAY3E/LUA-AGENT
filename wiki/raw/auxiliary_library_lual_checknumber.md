# luaL_checknumber

**Category**: Auxiliary Library

### `luaL_checknumber`[-0, +0, *v*]

```lua
lua_Number luaL_checknumber (lua_State *L, int arg);
```

Checks whether the function argument `arg` is a number and returns this number converted to a `lua_Number`.