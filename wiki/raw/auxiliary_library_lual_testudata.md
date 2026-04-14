# luaL_testudata

**Category**: Auxiliary Library

### `luaL_testudata`[-0, +0, *m*]

```lua
void *luaL_testudata (lua_State *L, int arg, const char *tname);
```

This function works like [`luaL_checkudata`](#luaL_checkudata), except that, when the test fails, it returns `NULL` instead of raising an error.