# luaL_buffsub

**Category**: Auxiliary Library

### `luaL_buffsub`[-?, +?, –]

```lua
void luaL_buffsub (luaL_Buffer *B, int n);
```

Removes `n` bytes from the buffer `B` (see [`luaL_Buffer`](#luaL_Buffer)). The buffer must have at least that many bytes.