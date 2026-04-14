# lua_tointegerx

**Category**: API

### `lua_tointegerx`[-0, +0, –]

```lua
lua_Integer lua_tointegerx (lua_State *L, int index, int *isnum);
```

Converts the Lua value at the given index to the signed integral type [`lua_Integer`](#lua_Integer). The Lua value must be an integer, or a number or string convertible to an integer (see [§3.4.3](#3.4.3)); otherwise, `lua_tointegerx` returns 0.

If `isnum` is not `NULL`, its referent is assigned a boolean value that indicates whether the operation succeeded.