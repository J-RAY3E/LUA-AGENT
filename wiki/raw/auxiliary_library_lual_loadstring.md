# luaL_loadstring

**Category**: Auxiliary Library

### `luaL_loadstring`[-0, +1, –]

```lua
int luaL_loadstring (lua_State *L, const char *s);
```

Loads a string as a Lua chunk. This function uses [`lua_load`](#lua_load) to load the chunk in the zero-terminated string `s`.

This function returns the same results as [`lua_load`](#lua_load).

Also as [`lua_load`](#lua_load), this function only loads the chunk; it does not run it.