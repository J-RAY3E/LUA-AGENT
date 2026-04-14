# lua_pcallk

**Category**: API

### `lua_pcallk`[-(nargs + 1), +(nresults|1), –]

```lua
int lua_pcallk (lua_State *L,
                int nargs,
                int nresults,
                int msgh,
                lua_KContext ctx,
                lua_KFunction k);
```

This function behaves exactly like [`lua_pcall`](#lua_pcall), except that it allows the called function to yield (see [§4.5](#4.5)).