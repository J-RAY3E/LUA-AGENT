# lua_isfunction

**Category**: API

### `lua_isfunction`[-0, +0, –]

```lua
int lua_isfunction (lua_State *L, int index);
```

Returns 1 if the value at the given index is a function (either C or Lua), and 0 otherwise.