# luaL_loadbufferx

**Category**: Auxiliary Library

### `luaL_loadbufferx`[-0, +1, –]

```lua
int luaL_loadbufferx (lua_State *L,
                      const char *buff,
                      size_t sz,
                      const char *name,
                      const char *mode);
```

Loads a buffer as a Lua chunk. This function uses [`lua_load`](#lua_load) to load the chunk in the buffer pointed to by `buff` with size `sz`.

This function returns the same results as [`lua_load`](#lua_load). `name` is the chunk name, used for debug information and error messages. The string `mode` works as in the function [`lua_load`](#lua_load). In particular, this function supports mode '`B`' for fixed buffers.