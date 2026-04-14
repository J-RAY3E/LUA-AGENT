# luaL_loadfile

**Category**: Auxiliary Library

### `luaL_loadfile`[-0, +1, *m*]

```lua
int luaL_loadfile (lua_State *L, const char *filename);
```

Equivalent to [`luaL_loadfilex`](#luaL_loadfilex) with `mode` equal to `NULL`.