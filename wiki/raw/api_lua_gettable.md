# lua_gettable

**Category**: API

### `lua_gettable`[-1, +1, *e*]

```lua
int lua_gettable (lua_State *L, int index);
```

Pushes onto the stack the value `t[k]`, where `t` is the value at the given index and `k` is the value on the top of the stack.

This function pops the key from the stack, pushing the resulting value in its place. As in Lua, this function may trigger a metamethod for the "index" event (see [§2.4](#2.4)).

Returns the type of the pushed value.