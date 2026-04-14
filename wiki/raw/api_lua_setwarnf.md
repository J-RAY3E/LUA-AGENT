# lua_setwarnf

**Category**: API

### `lua_setwarnf`[-0, +0, –]

```lua
void lua_setwarnf (lua_State *L, lua_WarnFunction f, void *ud);
```

Sets the warning function to be used by Lua to emit warnings (see [`lua_WarnFunction`](#lua_WarnFunction)). The `ud` parameter sets the value `ud` passed to the warning function.