# lua_tothread

**Category**: API

### `lua_tothread`[-0, +0, –]

```lua
lua_State *lua_tothread (lua_State *L, int index);
```

Converts the value at the given index to a Lua thread (represented as `lua_State*`). This value must be a thread; otherwise, the function returns `NULL`.