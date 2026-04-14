# lua_close

**Category**: API

### `lua_close`[-0, +0, –]

```lua
void lua_close (lua_State *L);
```

Close all active to-be-closed variables in the main thread, release all objects in the given Lua state (calling the corresponding garbage-collection metamethods, if any), and frees all dynamic memory used by this state.

On several platforms, you may not need to call this function, because all resources are naturally released when the host program ends. On the other hand, long-running programs that create multiple states, such as daemons or web servers, will probably need to close states as soon as they are not needed.