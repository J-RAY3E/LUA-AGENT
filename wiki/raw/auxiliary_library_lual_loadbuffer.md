# luaL_loadbuffer

**Category**: Auxiliary Library

### `luaL_loadbuffer`[-0, +1, –]

```lua
int luaL_loadbuffer (lua_State *L,
                     const char *buff,
                     size_t sz,
                     const char *name);
```

Equivalent to [`luaL_loadbufferx`](#luaL_loadbufferx) with `mode` equal to `NULL`.