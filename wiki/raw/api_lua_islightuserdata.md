# lua_islightuserdata

**Category**: API

### `lua_islightuserdata`[-0, +0, –]

```lua
int lua_islightuserdata (lua_State *L, int index);
```

Returns 1 if the value at the given index is a light userdata, and 0 otherwise.