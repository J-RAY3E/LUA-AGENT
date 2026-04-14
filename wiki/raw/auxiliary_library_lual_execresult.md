# luaL_execresult

**Category**: Auxiliary Library

### `luaL_execresult`[-0, +3, *m*]

```lua
int luaL_execresult (lua_State *L, int stat);
```

This function produces the return values for process-related functions in the standard library ([`os.execute`](#pdf-os.execute) and [`io.close`](#pdf-io.close)).