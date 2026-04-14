# luaL_error

**Category**: Auxiliary Library

### `luaL_error`[-0, +0, *v*]

```lua
int luaL_error (lua_State *L, const char *fmt, ...);
```

Raises an error. The error message format is given by `fmt` plus any extra arguments, following the same rules of [`lua_pushfstring`](#lua_pushfstring). It also adds at the beginning of the message the file name and the line number where the error occurred, if this information is available.

This function never returns, but it is an idiom to use it in C functions as `return luaL_error(args)`.