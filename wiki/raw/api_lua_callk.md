# lua_callk

**Category**: API

### `lua_callk`[-(nargs + 1), +nresults, *e*]

```lua
void lua_callk (lua_State *L,
                int nargs,
                int nresults,
                lua_KContext ctx,
                lua_KFunction k);
```

This function behaves exactly like [`lua_call`](#lua_call), but allows the called function to yield (see [§4.5](#4.5)).