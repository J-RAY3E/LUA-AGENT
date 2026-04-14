# lua_len

**Category**: API

### `lua_len`[-0, +1, *e*]

```lua
void lua_len (lua_State *L, int index);
```

Returns the length of the value at the given index. It is equivalent to the '`#`' operator in Lua (see [§3.4.7](#3.4.7)) and may trigger a metamethod for the "length" event (see [§2.4](#2.4)). The result is pushed on the stack.