# luaL_addsize

**Category**: Auxiliary Library

### `luaL_addsize`[-?, +?, –]

```lua
void luaL_addsize (luaL_Buffer *B, size_t n);
```

Adds to the buffer `B` a string of length `n` previously copied to the buffer area (see [`luaL_prepbuffer`](#luaL_prepbuffer)).