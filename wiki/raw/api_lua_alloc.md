# lua_Alloc

**Category**: API

### `lua_Alloc`

```lua
typedef void * (*lua_Alloc) (void *ud,
                             void *ptr,
                             size_t osize,
                             size_t nsize);
```

The type of the memory-allocator function used by Lua states. The allocator function must provide a functionality similar to `realloc`, but not exactly the same. Its arguments are `ud`, an opaque pointer passed to [`lua_newstate`](#lua_newstate); `ptr`, a pointer to the block being allocated/reallocated/freed; `osize`, the original size of the block or some code about what is being allocated; and `nsize`, the new size of the block.

When `ptr` is not `NULL`, `osize` is the size of the block pointed by `ptr`, that is, the size given when it was allocated or reallocated.

When `ptr` is `NULL`, `osize` encodes the kind of object that Lua is allocating. `osize` is any of [`LUA_TSTRING`](#pdf-LUA_TSTRING), [`LUA_TTABLE`](#pdf-LUA_TTABLE), [`LUA_TFUNCTION`](#pdf-LUA_TFUNCTION), [`LUA_TUSERDATA`](#pdf-LUA_TUSERDATA), or [`LUA_TTHREAD`](#pdf-LUA_TTHREAD) when (and only when) Lua is creating a new object of that type. When `osize` is some other value, Lua is allocating memory for something else.

Lua assumes the following behavior from the allocator function:

When `nsize` is zero, the allocator must behave like `free` and then return `NULL`.

When `nsize` is not zero, the allocator must behave like `realloc`. In particular, the allocator returns `NULL` if and only if it cannot fulfill the request.

Here is a simple implementation for the allocator function, corresponding to the function [`luaL_alloc`](#luaL_alloc) from the auxiliary library.

```lua
void *luaL_alloc (void *ud, void *ptr, size_t osize,
                                       size_t nsize) {
  (void)ud;  (void)osize;  /* not used */
  if (nsize == 0) {
    free(ptr);
    return NULL;
  }
  else
    return realloc(ptr, nsize);
}
```

Note that ISO C ensures that `free(NULL)` has no effect and that `realloc(NULL,size)` is equivalent to `malloc(size)`.