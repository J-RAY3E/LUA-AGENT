# lua_newstate

**Category**: API

### `lua_newstate`[-0, +0, –]

```lua
lua_State *lua_newstate (lua_Alloc f, void *ud,
                                   unsigned int seed);
```

Creates a new independent state and returns its main thread. Returns `NULL` if it cannot create the state (due to lack of memory). The argument `f` is the allocator function; Lua will do all memory allocation for this state through this function (see [`lua_Alloc`](#lua_Alloc)). The second argument, `ud`, is an opaque pointer that Lua passes to the allocator in every call. The third argument, `seed`, is a seed for the hashing of strings.