# luaL_newlibtable

**Category**: Auxiliary Library

### `luaL_newlibtable`[-0, +1, *m*]

```lua
void luaL_newlibtable (lua_State *L, const luaL_Reg l[]);
```

Creates a new table with a size optimized to store all entries in the array `l` (but does not actually store them). It is intended to be used in conjunction with [`luaL_setfuncs`](#luaL_setfuncs) (see [`luaL_newlib`](#luaL_newlib)).

It is implemented as a macro. The array `l` must be the actual array, not a pointer to it.