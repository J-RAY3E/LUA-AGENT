# luaL_prepbuffsize

**Category**: Auxiliary Library

### `luaL_prepbuffsize`[-?, +?, *m*]

```lua
char *luaL_prepbuffsize (luaL_Buffer *B, size_t sz);
```

Returns an address to a space of size `sz` where you can copy a string to be added to buffer `B` (see [`luaL_Buffer`](#luaL_Buffer)). After copying the string into this space you must call [`luaL_addsize`](#luaL_addsize) with the size of the string to actually add it to the buffer.