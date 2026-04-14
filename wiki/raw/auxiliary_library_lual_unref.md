# luaL_unref

**Category**: Auxiliary Library

### `luaL_unref`[-0, +0, –]

```lua
void luaL_unref (lua_State *L, int t, int ref);
```

Releases a reference (see [`luaL_ref`](#luaL_ref)). The integer `ref` must be either [`LUA_NOREF`](#pdf-LUA_NOREF), [`LUA_REFNIL`](#pdf-LUA_REFNIL), or a reference previously returned by [`luaL_ref`](#luaL_ref) and not already released. If `ref` is either [`LUA_NOREF`](#pdf-LUA_NOREF) or [`LUA_REFNIL`](#pdf-LUA_REFNIL) this function does nothing. Otherwise, the entry is removed from the table, so that the referred object can be collected and the reference `ref` can be used again by [`luaL_ref`](#luaL_ref).