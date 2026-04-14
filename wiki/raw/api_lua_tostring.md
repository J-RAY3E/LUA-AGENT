# lua_tostring

**Category**: API

### `lua_tostring`[-0, +0, *m*]

```lua
const char *lua_tostring (lua_State *L, int index);
```

Equivalent to [`lua_tolstring`](#lua_tolstring) with `len` equal to `NULL`.