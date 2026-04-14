# lua_pushthread

**Category**: API

### `lua_pushthread`[-0, +1, –]

```lua
int lua_pushthread (lua_State *L);
```

Pushes the thread represented by `L` onto the stack. Returns 1 if this thread is the main thread of its state.