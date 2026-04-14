# luaL_newstate

**Category**: Auxiliary Library

### `luaL_newstate`[-0, +0, –]

```lua
lua_State *luaL_newstate (void);
```

Creates a new Lua state. It calls [`lua_newstate`](#lua_newstate) with [`luaL_alloc`](#luaL_alloc) as the allocator function and the result of `luaL_makeseed(NULL)` as the seed, and then sets a warning function and a panic function (see [§4.4](#4.4)) that print messages to the standard error output.

Returns the new state, or `NULL` if there is a memory allocation error.