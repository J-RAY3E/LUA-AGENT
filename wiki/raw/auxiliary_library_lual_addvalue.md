# luaL_addvalue

**Category**: Auxiliary Library

### `luaL_addvalue`[-?, +?, *m*]

```lua
void luaL_addvalue (luaL_Buffer *B);
```

Adds the value on the top of the stack to the buffer `B` (see [`luaL_Buffer`](#luaL_Buffer)). Pops the value.

This is the only function on string buffers that can (and must) be called with an extra element on the stack, which is the value to be added to the buffer.