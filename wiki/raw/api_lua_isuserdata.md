# lua_isuserdata

**Category**: API

### `lua_isuserdata`[-0, +0, –]

```lua
int lua_isuserdata (lua_State *L, int index);
```

Returns 1 if the value at the given index is a userdata (either full or light), and 0 otherwise.