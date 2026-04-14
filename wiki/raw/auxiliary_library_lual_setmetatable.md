# luaL_setmetatable

**Category**: Auxiliary Library

### `luaL_setmetatable`[-0, +0, –]

```lua
void luaL_setmetatable (lua_State *L, const char *tname);
```

Sets the metatable of the object on the top of the stack as the metatable associated with name `tname` in the registry (see [`luaL_newmetatable`](#luaL_newmetatable)).