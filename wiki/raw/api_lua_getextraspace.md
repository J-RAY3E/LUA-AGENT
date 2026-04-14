# lua_getextraspace

**Category**: API

### `lua_getextraspace`[-0, +0, –]

```lua
void *lua_getextraspace (lua_State *L);
```

Returns a pointer to a raw memory area associated with the given Lua state. The application can use this area for any purpose; Lua does not use it for anything.

Each new thread has this area initialized with a copy of the area of the main thread.

By default, this area has the size of a pointer to void, but you can recompile Lua with a different size for this area. (See `LUA_EXTRASPACE` in `luaconf.h`.)