# lua_topointer

**Category**: API

### `lua_topointer`[-0, +0, –]

```lua
const void *lua_topointer (lua_State *L, int index);
```

Converts the value at the given index to a generic C pointer (`void*`). The value can be a userdata, a table, a thread, a string, or a function; otherwise, `lua_topointer` returns `NULL`. Different objects will give different pointers. There is no way to convert the pointer back to its original value.

Typically this function is used only for hashing and debug information.