# lua_pushvalue

**Category**: API

### `lua_pushvalue`[-0, +1, –]

```lua
void lua_pushvalue (lua_State *L, int index);
```

Pushes a copy of the element at the given index onto the stack.