# lua_tonumberx

**Category**: API

### `lua_tonumberx`[-0, +0, –]

```lua
lua_Number lua_tonumberx (lua_State *L, int index, int *isnum);
```

Converts the Lua value at the given index to the C type [`lua_Number`](#lua_Number) (see [`lua_Number`](#lua_Number)). The Lua value must be a number or a string convertible to a number (see [§3.4.3](#3.4.3)); otherwise, [`lua_tonumberx`](#lua_tonumberx) returns 0.

If `isnum` is not `NULL`, its referent is assigned a boolean value that indicates whether the operation succeeded.