# luaL_argcheck

**Category**: Auxiliary Library

### `luaL_argcheck`[-0, +0, *v*]

```lua
void luaL_argcheck (lua_State *L,
                    int cond,
                    int arg,
                    const char *extramsg);
```

Checks whether `cond` is true. If it is not, raises an error with a standard message (see [`luaL_argerror`](#luaL_argerror)).