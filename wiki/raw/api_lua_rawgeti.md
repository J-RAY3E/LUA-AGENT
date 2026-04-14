# lua_rawgeti

**Category**: API

### `lua_rawgeti`[-0, +1, –]

```lua
int lua_rawgeti (lua_State *L, int index, lua_Integer n);
```

Pushes onto the stack the value `t[n]`, where `t` is the table at the given index. The access is raw, that is, it does not use the `__index` metavalue.

Returns the type of the pushed value.