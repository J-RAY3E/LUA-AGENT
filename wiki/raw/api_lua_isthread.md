# lua_isthread

**Category**: API

### `lua_isthread`[-0, +0, –]

```lua
int lua_isthread (lua_State *L, int index);
```

Returns 1 if the value at the given index is a thread, and 0 otherwise.