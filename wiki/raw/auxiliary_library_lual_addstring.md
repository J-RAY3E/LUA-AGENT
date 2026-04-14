# luaL_addstring

**Category**: Auxiliary Library

### `luaL_addstring`[-?, +?, *m*]

```lua
void luaL_addstring (luaL_Buffer *B, const char *s);
```

Adds the zero-terminated string pointed to by `s` to the buffer `B` (see [`luaL_Buffer`](#luaL_Buffer)).