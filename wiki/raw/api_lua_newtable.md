# lua_newtable

**Category**: API

### `lua_newtable`[-0, +1, *m*]

```lua
void lua_newtable (lua_State *L);
```

Creates a new empty table and pushes it onto the stack. It is equivalent to `lua_createtable(L,0,0)`.