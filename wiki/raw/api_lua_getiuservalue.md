# lua_getiuservalue

**Category**: API

### `lua_getiuservalue`[-0, +1, –]

```lua
int lua_getiuservalue (lua_State *L, int index, int n);
```

Pushes onto the stack the `n`-th user value associated with the full userdata at the given index and returns the type of the pushed value.

If the userdata does not have that value, pushes **nil** and returns [`LUA_TNONE`](#pdf-LUA_TNONE).