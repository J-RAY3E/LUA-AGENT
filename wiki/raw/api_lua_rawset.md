# lua_rawset

**Category**: API

### `lua_rawset`[-2, +0, *m*]

```lua
void lua_rawset (lua_State *L, int index);
```

Similar to [`lua_settable`](#lua_settable), but does a raw assignment (i.e., without metamethods). The value at `index` must be a table.