# luaL_prepbuffer

**Category**: Auxiliary Library

### `luaL_prepbuffer`[-?, +?, *m*]

```lua
char *luaL_prepbuffer (luaL_Buffer *B);
```

Equivalent to [`luaL_prepbuffsize`](#luaL_prepbuffsize) with the predefined size `LUAL_BUFFERSIZE`.