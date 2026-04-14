# lua_toboolean

**Category**: API

### `lua_toboolean`[-0, +0, –]

```lua
int lua_toboolean (lua_State *L, int index);
```

Converts the Lua value at the given index to a C boolean value (0 or 1). Like all tests in Lua, [`lua_toboolean`](#lua_toboolean) returns true for any Lua value different from **false** and **nil**; otherwise it returns false. (If you want to accept only actual boolean values, use [`lua_isboolean`](#lua_isboolean) to test the value's type.)