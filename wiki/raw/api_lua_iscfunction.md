# lua_iscfunction

**Category**: API

### `lua_iscfunction`[-0, +0, –]

```lua
int lua_iscfunction (lua_State *L, int index);
```

Returns 1 if the value at the given index is a C function, and 0 otherwise.