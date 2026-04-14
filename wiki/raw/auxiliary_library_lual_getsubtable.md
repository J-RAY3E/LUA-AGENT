# luaL_getsubtable

**Category**: Auxiliary Library

### `luaL_getsubtable`[-0, +1, *e*]

```lua
int luaL_getsubtable (lua_State *L, int idx, const char *fname);
```

Ensures that the value `t[fname]`, where `t` is the value at index `idx`, is a table, and pushes that table onto the stack. Returns true if it finds a previous table there and false if it creates a new table.