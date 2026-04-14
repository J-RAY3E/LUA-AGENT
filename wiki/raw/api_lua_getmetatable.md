# lua_getmetatable

**Category**: API

### `lua_getmetatable`[-0, +(0|1), –]

```lua
int lua_getmetatable (lua_State *L, int index);
```

If the value at the given index has a metatable, the function pushes that metatable onto the stack and returns 1. Otherwise, the function returns 0 and pushes nothing on the stack.