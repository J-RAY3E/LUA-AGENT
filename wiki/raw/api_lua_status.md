# lua_status

**Category**: API

### `lua_status`[-0, +0, –]

```lua
int lua_status (lua_State *L);
```

Returns the status of the thread `L`.

The status can be [`LUA_OK`](#pdf-LUA_OK) for a normal thread, an error code if the thread finished the execution of a [`lua_resume`](#lua_resume) with an error, or [`LUA_YIELD`](#pdf-LUA_YIELD) if the thread is suspended.

You can call functions only in threads with status [`LUA_OK`](#pdf-LUA_OK). You can resume threads with status [`LUA_OK`](#pdf-LUA_OK) (to start a new coroutine) or [`LUA_YIELD`](#pdf-LUA_YIELD) (to resume a coroutine).