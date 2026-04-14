# luaL_checktype

**Category**: Auxiliary Library

### `luaL_checktype`[-0, +0, *v*]

```lua
void luaL_checktype (lua_State *L, int arg, int t);
```

Checks whether the function argument `arg` has type `t`. See [`lua_type`](#lua_type) for the encoding of types for `t`.