# luaL_makeseed

**Category**: Auxiliary Library

### `luaL_makeseed`[-0, +0, –]

```lua
unsigned int luaL_makeseed (lua_State *L);
```

Returns a value with a weak attempt for randomness. The parameter `L` can be `NULL` if there is no Lua state available.