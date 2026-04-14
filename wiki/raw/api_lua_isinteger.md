# lua_isinteger

**Category**: API

### `lua_isinteger`[-0, +0, –]

```lua
int lua_isinteger (lua_State *L, int index);
```

Returns 1 if the value at the given index is an integer (that is, the value is a number and is represented as an integer), and 0 otherwise.