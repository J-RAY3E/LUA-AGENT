# luaL_Reg

**Category**: Auxiliary Library

### `luaL_Reg`

```lua
typedef struct luaL_Reg {
  const char *name;
  lua_CFunction func;
} luaL_Reg;
```

Type for arrays of functions to be registered by [`luaL_setfuncs`](#luaL_setfuncs). `name` is the function name and `func` is a pointer to the function. Any array of [`luaL_Reg`](#luaL_Reg) must end with a sentinel entry in which both `name` and `func` are `NULL`.