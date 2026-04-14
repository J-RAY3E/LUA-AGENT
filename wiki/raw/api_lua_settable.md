# lua_settable

**Category**: API

### `lua_settable`[-2, +0, *e*]

```lua
void lua_settable (lua_State *L, int index);
```

Does the equivalent to `t[k] = v`, where `t` is the value at the given index, `v` is the value on the top of the stack, and `k` is the value just below the top.

This function pops both the key and the value from the stack. As in Lua, this function may trigger a metamethod for the "newindex" event (see [§2.4](#2.4)).