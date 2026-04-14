# luaL_len

**Category**: Auxiliary Library

### `luaL_len`[-0, +0, *e*]

```lua
lua_Integer luaL_len (lua_State *L, int index);
```

Returns the "length" of the value at the given index as a number; it is equivalent to the '`#`' operator in Lua (see [§3.4.7](#3.4.7)). Raises an error if the result of the operation is not an integer. (This case can only happen through metamethods.)