# lua_tointeger

**Category**: API

### `lua_tointeger`[-0, +0, –]

```lua
lua_Integer lua_tointeger (lua_State *L, int index);
```

Equivalent to [`lua_tointegerx`](#lua_tointegerx) with `isnum` equal to `NULL`.