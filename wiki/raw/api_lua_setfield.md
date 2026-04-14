# lua_setfield

**Category**: API

### `lua_setfield`[-1, +0, *e*]

```lua
void lua_setfield (lua_State *L, int index, const char *k);
```

Does the equivalent to `t[k] = v`, where `t` is the value at the given index and `v` is the value on the top of the stack.

This function pops the value from the stack. As in Lua, this function may trigger a metamethod for the "newindex" event (see [§2.4](#2.4)).