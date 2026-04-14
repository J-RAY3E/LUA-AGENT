# lua_yield

**Category**: API

### `lua_yield`[-?, +?, *v*]

```lua
int lua_yield (lua_State *L, int nresults);
```

This function is equivalent to [`lua_yieldk`](#lua_yieldk), but it has no continuation (see [§4.5](#4.5)). Therefore, when the thread resumes, it continues the function that called the function calling `lua_yield`. To avoid surprises, this function should be called only in a tail call.