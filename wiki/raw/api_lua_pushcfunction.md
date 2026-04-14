# lua_pushcfunction

**Category**: API

### `lua_pushcfunction`[-0, +1, –]

```lua
void lua_pushcfunction (lua_State *L, lua_CFunction f);
```

Pushes a C function onto the stack. This function is equivalent to [`lua_pushcclosure`](#lua_pushcclosure) with no upvalues.