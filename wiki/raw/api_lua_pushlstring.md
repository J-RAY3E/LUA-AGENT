# lua_pushlstring

**Category**: API

### `lua_pushlstring`[-0, +1, *v*]

```lua
const char *lua_pushlstring (lua_State *L, const char *s, size_t len);
```

Pushes the string pointed to by `s` with size `len` onto the stack. Lua will make or reuse an internal copy of the given string, so the memory at `s` can be freed or reused immediately after the function returns. The string can contain any binary data, including embedded zeros.

Returns a pointer to the internal copy of the string (see [§4.1.3](#4.1.3)).

Besides memory allocation errors, this function may raise an error if the string is too large.