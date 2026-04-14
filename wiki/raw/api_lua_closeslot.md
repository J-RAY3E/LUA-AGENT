# lua_closeslot

**Category**: API

### `lua_closeslot`[-0, +0, *e*]

```lua
void lua_closeslot (lua_State *L, int index);
```

Close the to-be-closed slot at the given index and set its value to **nil**. The index must be the last index previously marked to be closed (see [`lua_toclose`](#lua_toclose)) that is still active (that is, not closed yet).

A `__close` metamethod cannot yield when called through this function.