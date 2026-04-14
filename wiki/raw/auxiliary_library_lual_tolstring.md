# luaL_tolstring

**Category**: Auxiliary Library

### `luaL_tolstring`[-0, +1, *e*]

```lua
const char *luaL_tolstring (lua_State *L, int idx, size_t *len);
```

Converts any Lua value at the given index to a C string in a reasonable format. The resulting string is pushed onto the stack and also returned by the function (see [§4.1.3](#4.1.3)). If `len` is not `NULL`, the function also sets `*len` with the string length.

If the value has a metatable with a `__tostring` field, then `luaL_tolstring` calls the corresponding metamethod with the value as argument, and uses the result of the call as its result.