# lua_isnoneornil

**Category**: API

### `lua_isnoneornil`[-0, +0, –]

```lua
int lua_isnoneornil (lua_State *L, int index);
```

Returns 1 if the given index is not valid or if the value at this index is **nil**, and 0 otherwise.