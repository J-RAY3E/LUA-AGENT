# lua_compare

**Category**: API

### `lua_compare`[-0, +0, *e*]

```lua
int lua_compare (lua_State *L, int index1, int index2, int op);
```

Compares two Lua values. Returns 1 if the value at index `index1` satisfies `op` when compared with the value at index `index2`, following the semantics of the corresponding Lua operator (that is, it may call metamethods). Otherwise returns 0. Also returns 0 if any of the indices is not valid.

The value of `op` must be one of the following constants:

* **`LUA_OPEQ`**: compares for equality (`==`)
* **`LUA_OPLT`**: compares for less than (`<`)
* **`LUA_OPLE`**: compares for less or equal (`<=`)