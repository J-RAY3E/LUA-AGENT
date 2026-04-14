# lua_getfield

**Category**: API

### `lua_getfield`[-0, +1, *e*]

```lua
int lua_getfield (lua_State *L, int index, const char *k);
```

Pushes onto the stack the value `t[k]`, where `t` is the value at the given index. As in Lua, this function may trigger a metamethod for the "index" event (see [§2.4](#2.4)).

Returns the type of the pushed value.