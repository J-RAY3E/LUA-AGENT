# luaL_pushresult

**Category**: Auxiliary Library

### `luaL_pushresult`[-?, +1, *m*]

```lua
void luaL_pushresult (luaL_Buffer *B);
```

Finishes the use of buffer `B` leaving the final string on the top of the stack.