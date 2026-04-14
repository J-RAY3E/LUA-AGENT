# lua_isstring

**Category**: API

### `lua_isstring`[-0, +0, –]

```lua
int lua_isstring (lua_State *L, int index);
```

Returns 1 if the value at the given index is a string or a number (which is always convertible to a string), and 0 otherwise.