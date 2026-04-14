# lua_pushvfstring

**Category**: API

### `lua_pushvfstring`[-0, +1, –]

```lua
const char *lua_pushvfstring (lua_State *L,
                              const char *fmt,
                              va_list argp);
```

Equivalent to [`lua_pushfstring`](#lua_pushfstring), except that it receives a `va_list` instead of a variable number of arguments, and it does not raise errors. Instead, in case of errors it pushes the error message and returns `NULL`.