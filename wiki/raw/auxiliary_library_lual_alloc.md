# luaL_alloc

**Category**: Auxiliary Library

### `luaL_alloc`

```lua
void *luaL_alloc (void *ud, void *ptr, size_t osize, size_t nsize);
```

A standard allocator function for Lua (see [`lua_Alloc`](#lua_Alloc)), built on top of the C functions `realloc` and `free`.