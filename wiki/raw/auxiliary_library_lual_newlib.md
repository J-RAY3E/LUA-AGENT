# luaL_newlib

**Category**: Auxiliary Library

### `luaL_newlib`[-0, +1, *m*]

```lua
void luaL_newlib (lua_State *L, const luaL_Reg l[]);
```

Creates a new table and registers there the functions in the list `l`.

It is implemented as the following macro:

```lua
(luaL_newlibtable(L,l), luaL_setfuncs(L,l,0))
```

The array `l` must be the actual array, not a pointer to it.