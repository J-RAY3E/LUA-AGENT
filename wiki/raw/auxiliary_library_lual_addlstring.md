# luaL_addlstring

**Category**: Auxiliary Library

### `luaL_addlstring`[-?, +?, *m*]

```lua
void luaL_addlstring (luaL_Buffer *B, const char *s, size_t l);
```

Adds the string pointed to by `s` with length `l` to the buffer `B` (see [`luaL_Buffer`](#luaL_Buffer)). The string can contain embedded zeros.