# luaL_optnumber

**Category**: Auxiliary Library

### `luaL_optnumber`[-0, +0, *v*]

```lua
lua_Number luaL_optnumber (lua_State *L, int arg, lua_Number d);
```

If the function argument `arg` is a number, returns this number as a `lua_Number`. If this argument is absent or is **nil**, returns `d`. Otherwise, raises an error.