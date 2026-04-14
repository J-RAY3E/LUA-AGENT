# lua_newuserdatauv

**Category**: API

### `lua_newuserdatauv`[-0, +1, *m*]

```lua
void *lua_newuserdatauv (lua_State *L, size_t size, int nuvalue);
```

This function creates and pushes on the stack a new full userdata, with `nuvalue` associated Lua values, called `user values`, plus an associated block of raw memory with `size` bytes. (The user values can be set and read with the functions [`lua_setiuservalue`](#lua_setiuservalue) and [`lua_getiuservalue`](#lua_getiuservalue).)

The function returns the address of the block of memory. Lua ensures that this address is valid as long as the corresponding userdata is alive (see [§2.5](#2.5)). Moreover, if the userdata is marked for finalization (see [§2.5.3](#2.5.3)), its address is valid at least until the call to its finalizer.