# lua_atpanic

**Category**: API

### `lua_atpanic`[-0, +0, –]

```lua
lua_CFunction lua_atpanic (lua_State *L, lua_CFunction panicf);
```

Sets a new panic function and returns the old one (see [§4.4](#4.4)).