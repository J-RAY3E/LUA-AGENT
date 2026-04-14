# lua_setmetatable

**Category**: API

### `lua_setmetatable`[-1, +0, –]

```lua
int lua_setmetatable (lua_State *L, int index);
```

Pops a table or **nil** from the stack and sets that value as the new metatable for the value at the given index. (**nil** means no metatable.)

(For historical reasons, this function returns an `int`, which now is always 1.)