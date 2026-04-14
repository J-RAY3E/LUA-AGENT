# luaL_argerror

**Category**: Auxiliary Library

### `luaL_argerror`[-0, +0, *v*]

```lua
int luaL_argerror (lua_State *L, int arg, const char *extramsg);
```

Raises an error reporting a problem with argument `arg` of the C function that called it, using a standard message that includes `extramsg` as a comment:

```lua
bad argument #arg to 'funcname' (extramsg)
```

This function never returns.