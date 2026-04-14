# luaL_buffinit

**Category**: Auxiliary Library

### `luaL_buffinit`[-0, +?, –]

```lua
void luaL_buffinit (lua_State *L, luaL_Buffer *B);
```

Initializes a buffer `B` (see [`luaL_Buffer`](#luaL_Buffer)). This function does not allocate any space; the buffer must be declared as a variable.