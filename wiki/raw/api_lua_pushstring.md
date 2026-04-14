# lua_pushstring

**Category**: API

### `lua_pushstring`[-0, +1, *m*]

```lua
const char *lua_pushstring (lua_State *L, const char *s);
```

Pushes the zero-terminated string pointed to by `s` onto the stack. Lua will make or reuse an internal copy of the given string, so the memory at `s` can be freed or reused immediately after the function returns.

Returns a pointer to the internal copy of the string (see [§4.1.3](#4.1.3)).

If `s` is `NULL`, pushes **nil** and returns `NULL`.