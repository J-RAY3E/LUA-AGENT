# luaL_checkany

**Category**: Auxiliary Library

### `luaL_checkany`[-0, +0, *v*]

```lua
void luaL_checkany (lua_State *L, int arg);
```

Checks whether the function has an argument of any type (including **nil**) at position `arg`.