# lua_toclose

**Category**: API

### `lua_toclose`[-0, +0, *v*]

```lua
void lua_toclose (lua_State *L, int index);
```

Marks the given index in the stack as a to-be-closed slot (see [§3.3.8](#3.3.8)). Like a to-be-closed variable in Lua, the value at that slot in the stack will be closed when it goes out of scope. Here, in the context of a C function, to go out of scope means that the running function returns to Lua, or there is an error, or the slot is removed from the stack through [`lua_settop`](#lua_settop) or [`lua_pop`](#lua_pop), or there is a call to [`lua_closeslot`](#lua_closeslot). A slot marked as to-be-closed should not be removed from the stack by any other function in the API except [`lua_settop`](#lua_settop) or [`lua_pop`](#lua_pop), unless previously deactivated by [`lua_closeslot`](#lua_closeslot).

This function raises an error if the value at the given slot neither has a `__close` metamethod nor is a false value.

This function should not be called for an index that is equal to or below an active to-be-closed slot.

Note that, both in case of errors and of a regular return, by the time the `__close` metamethod runs, the C stack was already unwound, so that any automatic C variable declared in the calling function (e.g., a buffer) will be out of scope.