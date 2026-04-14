# luaL_getmetatable

**Category**: Auxiliary Library

### `luaL_getmetatable`[-0, +1, *m*]

```lua
int luaL_getmetatable (lua_State *L, const char *tname);
```

Pushes onto the stack the metatable associated with the name `tname` in the registry (see [`luaL_newmetatable`](#luaL_newmetatable)), or **nil** if there is no metatable associated with that name. Returns the type of the pushed value.