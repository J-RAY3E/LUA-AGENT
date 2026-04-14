# luaL_buffaddr

**Category**: Auxiliary Library

### `luaL_buffaddr`[-0, +0, –]

```lua
char *luaL_buffaddr (luaL_Buffer *B);
```

Returns the address of the current content of buffer `B` (see [`luaL_Buffer`](#luaL_Buffer)). Note that any addition to the buffer may invalidate this address.