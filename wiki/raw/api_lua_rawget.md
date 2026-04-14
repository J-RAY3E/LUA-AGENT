# lua_rawget

**Category**: API

### `lua_rawget`[-1, +1, –]

```lua
int lua_rawget (lua_State *L, int index);
```

Similar to [`lua_gettable`](#lua_gettable), but does a raw access (i.e., without metamethods). The value at `index` must be a table.