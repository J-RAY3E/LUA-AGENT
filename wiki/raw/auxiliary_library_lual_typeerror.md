# luaL_typeerror

**Category**: Auxiliary Library

### `luaL_typeerror`[-0, +0, *v*]

```lua
int luaL_typeerror (lua_State *L, int arg, const char *tname);
```

Raises a type error for the argument `arg` of the C function that called it, using a standard message; `tname` is a "name" for the expected type. This function never returns.