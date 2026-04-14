# luaL_dofile

**Category**: Auxiliary Library

### `luaL_dofile`[-0, +?, *m*]

```lua
int luaL_dofile (lua_State *L, const char *filename);
```

Loads and runs the given file. It is defined as the following macro:

```lua
(luaL_loadfile(L, filename) || lua_pcall(L, 0, LUA_MULTRET, 0))
```

It returns 0 ([`LUA_OK`](#pdf-LUA_OK)) if there are no errors, or 1 in case of errors. (Except for out-of-memory errors, which are raised.)