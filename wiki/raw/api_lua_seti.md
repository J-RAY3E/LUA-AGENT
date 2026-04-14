# lua_seti

**Category**: API

### `lua_seti`[-1, +0, *e*]

```lua
void lua_seti (lua_State *L, int index, lua_Integer n);
```

Does the equivalent to `t[n] = v`, where `t` is the value at the given index and `v` is the value on the top of the stack.

This function pops the value from the stack. As in Lua, this function may trigger a metamethod for the "newindex" event (see [§2.4](#2.4)).