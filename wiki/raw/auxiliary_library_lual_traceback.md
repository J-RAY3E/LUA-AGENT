# luaL_traceback

**Category**: Auxiliary Library

### `luaL_traceback`[-0, +1, *m*]

```lua
void luaL_traceback (lua_State *L, lua_State *L1, const char *msg,
                     int level);
```

Creates and pushes a traceback of the stack `L1`. If `msg` is not `NULL`, it is appended at the beginning of the traceback. The `level` parameter tells at which level to start the traceback.