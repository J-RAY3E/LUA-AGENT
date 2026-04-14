# lua_geti

**Category**: API

### `lua_geti`[-0, +1, *e*]

```lua
int lua_geti (lua_State *L, int index, lua_Integer i);
```

Pushes onto the stack the value `t[i]`, where `t` is the value at the given index. As in Lua, this function may trigger a metamethod for the "index" event (see [§2.4](#2.4)).

Returns the type of the pushed value.