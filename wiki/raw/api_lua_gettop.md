# lua_gettop

**Category**: API

### `lua_gettop`[-0, +0, –]

```lua
int lua_gettop (lua_State *L);
```

Returns the index of the top element in the stack. Because indices start at 1, this result is equal to the number of elements in the stack; in particular, 0 means an empty stack.