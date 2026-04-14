# luaL_argexpected

**Category**: Auxiliary Library

### `luaL_argexpected`[-0, +0, *v*]

```lua
void luaL_argexpected (lua_State *L,
                       int cond,
                       int arg,
                       const char *tname);
```

Checks whether `cond` is true. If it is not, raises an error about the type of the argument `arg` with a standard message (see [`luaL_typeerror`](#luaL_typeerror)).