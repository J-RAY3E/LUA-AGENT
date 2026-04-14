# lua_touserdata

**Category**: API

### `lua_touserdata`[-0, +0, –]

```lua
void *lua_touserdata (lua_State *L, int index);
```

If the value at the given index is a full userdata, returns its memory-block address. If the value is a light userdata, returns its value (a pointer). Otherwise, returns `NULL`.