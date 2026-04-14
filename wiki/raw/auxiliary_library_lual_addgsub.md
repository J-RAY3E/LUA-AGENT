# luaL_addgsub

**Category**: Auxiliary Library

### `luaL_addgsub`[-?, +?, *m*]

```lua
const void luaL_addgsub (luaL_Buffer *B, const char *s,
                         const char *p, const char *r);
```

Adds a copy of the string `s` to the buffer `B` (see [`luaL_Buffer`](#luaL_Buffer)), replacing any occurrence of the string `p` with the string `r`.