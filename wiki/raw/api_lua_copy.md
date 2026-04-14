# lua_copy

**Category**: API

### `lua_copy`[-0, +0, –]

```lua
void lua_copy (lua_State *L, int fromidx, int toidx);
```

Copies the element at index `fromidx` into the valid index `toidx`, replacing the value at that position. Values at other positions are not affected.