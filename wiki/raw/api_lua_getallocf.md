# lua_getallocf

**Category**: API

### `lua_getallocf`[-0, +0, –]

```lua
lua_Alloc lua_getallocf (lua_State *L, void **ud);
```

Returns the memory-allocator function of a given state. If `ud` is not `NULL`, Lua stores in `*ud` the opaque pointer given when the memory-allocator function was set.