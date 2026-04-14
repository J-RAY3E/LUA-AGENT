# lua_isnumber

**Category**: API

### `lua_isnumber`[-0, +0, –]

```lua
int lua_isnumber (lua_State *L, int index);
```

Returns 1 if the value at the given index is a number or a string convertible to a number, and 0 otherwise.