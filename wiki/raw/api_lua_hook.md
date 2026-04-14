# lua_Hook

**Category**: API

### `lua_Hook`

```lua
typedef void (*lua_Hook) (lua_State *L, lua_Debug *ar);
```

Type for debugging hook functions.

Whenever a hook is called, its `ar` argument has its field `event` set to the specific event that triggered the hook. Lua identifies these events with the following constants: `LUA_HOOKCALL`, `LUA_HOOKRET`, `LUA_HOOKTAILCALL`, `LUA_HOOKLINE`, and `LUA_HOOKCOUNT`. Moreover, for line events, the field `currentline` is also set. To get the value of any other field in `ar`, the hook must call [`lua_getinfo`](#lua_getinfo).

For call events, `event` can be `LUA_HOOKCALL`, the normal value, or `LUA_HOOKTAILCALL`, for a tail call; in this case, there will be no corresponding return event.

While Lua is running a hook, it disables other calls to hooks. Therefore, if a hook calls back Lua to execute a function or a chunk, this execution occurs without any calls to hooks.

Hook functions cannot have continuations, that is, they cannot call [`lua_yieldk`](#lua_yieldk), [`lua_pcallk`](#lua_pcallk), or [`lua_callk`](#lua_callk) with a non-null `k`.

Hook functions can yield under the following conditions: Only count and line events can yield; to yield, a hook function must finish its execution calling [`lua_yield`](#lua_yield) with `nresults` equal to zero (that is, with no values).