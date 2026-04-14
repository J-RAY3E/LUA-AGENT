# lua_newthread

**Category**: API

### `lua_newthread`[-0, +1, *m*]

```lua
lua_State *lua_newthread (lua_State *L);
```

Creates a new thread, pushes it on the stack, and returns a pointer to a [`lua_State`](#lua_State) that represents this new thread. The new thread returned by this function shares with the original thread its global environment, but has an independent execution stack.

Threads are subject to garbage collection, like any Lua object.