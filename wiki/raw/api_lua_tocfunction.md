# lua_tocfunction

**Category**: API

### `lua_tocfunction`[-0, +0, –]

```lua
lua_CFunction lua_tocfunction (lua_State *L, int index);
```

Converts a value at the given index to a C function. That value must be a C function; otherwise, returns `NULL`.