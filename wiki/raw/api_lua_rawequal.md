# lua_rawequal

**Category**: API

### `lua_rawequal`[-0, +0, –]

```lua
int lua_rawequal (lua_State *L, int index1, int index2);
```

Returns 1 if the two values in indices `index1` and `index2` are primitively equal (that is, equal without calling the `__eq` metamethod). Otherwise returns 0. Also returns 0 if any of the indices are not valid.