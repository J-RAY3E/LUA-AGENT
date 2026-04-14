# lua_rawgetp

**Category**: API

### `lua_rawgetp`[-0, +1, –]

```lua
int lua_rawgetp (lua_State *L, int index, const void *p);
```

Pushes onto the stack the value `t[k]`, where `t` is the table at the given index and `k` is the pointer `p` represented as a light userdata. The access is raw; that is, it does not use the `__index` metavalue.

Returns the type of the pushed value.