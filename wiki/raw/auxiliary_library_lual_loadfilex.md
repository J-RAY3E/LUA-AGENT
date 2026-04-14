# luaL_loadfilex

**Category**: Auxiliary Library

### `luaL_loadfilex`[-0, +1, *m*]

```lua
int luaL_loadfilex (lua_State *L, const char *filename,
                                            const char *mode);
```

Loads a file as a Lua chunk. This function uses [`lua_load`](#lua_load) to load the chunk in the file named `filename`. If `filename` is `NULL`, then it loads from the standard input. The first line in the file is ignored if it starts with a `#`.

The string `mode` works as in the function [`lua_load`](#lua_load).

This function returns the same results as [`lua_load`](#lua_load), or [`LUA_ERRFILE`](#pdf-LUA_ERRFILE) for file-related errors.

As [`lua_load`](#lua_load), this function only loads the chunk; it does not run it.