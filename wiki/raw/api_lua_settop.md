# lua_settop

**Category**: API

### `lua_settop`[-?, +?, *e*]

```lua
void lua_settop (lua_State *L, int index);
```

Receives any acceptable stack index, or 0, and sets the stack top to this index. If the new top is greater than the old one, then the new elements are filled with **nil**. If `index` is 0, then all stack elements are removed.

This function can run arbitrary code when removing an index marked as to-be-closed from the stack.