# lua_error

**Category**: API

### `lua_error`[-1, +0, *v*]

```lua
int lua_error (lua_State *L);
```

Raises a Lua error, using the value on the top of the stack as the error object. This function does a long jump, and therefore never returns (see [`luaL_error`](#luaL_error)).