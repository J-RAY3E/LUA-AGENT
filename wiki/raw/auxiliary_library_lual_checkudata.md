# luaL_checkudata

**Category**: Auxiliary Library

### `luaL_checkudata`[-0, +0, *v*]

```lua
void *luaL_checkudata (lua_State *L, int arg, const char *tname);
```

Checks whether the function argument `arg` is a userdata of the type `tname` (see [`luaL_newmetatable`](#luaL_newmetatable)) and returns the userdata's memory-block address (see [`lua_touserdata`](#lua_touserdata)).