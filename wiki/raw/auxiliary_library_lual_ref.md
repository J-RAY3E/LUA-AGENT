# luaL_ref

**Category**: Auxiliary Library

### `luaL_ref`[-1, +0, *m*]

```lua
int luaL_ref (lua_State *L, int t);
```

Creates and returns a *reference*, in the table at index `t`, for the object on the top of the stack (and pops the object).

The reference system uses the integer keys of the table. A reference is a unique integer key; [`luaL_ref`](#luaL_ref) ensures the uniqueness of the keys it returns. The entry 1 is reserved for internal use. Before the first use of [`luaL_ref`](#luaL_ref), the integer keys of the table should form a proper sequence (no holes), and the value at entry 1 should be false: **nil** if the sequence is empty, **false** otherwise. You should not manually set integer keys in the table after the first use of [`luaL_ref`](#luaL_ref).

You can retrieve an object referred by the reference `r` by calling `lua_rawgeti(L,t,r)` or `lua_geti(L,t,r)`. The function [`luaL_unref`](#luaL_unref) frees a reference.

If the object on the top of the stack is **nil**, [`luaL_ref`](#luaL_ref) returns the constant `LUA_REFNIL`. The constant `LUA_NOREF` is guaranteed to be different from any reference returned by [`luaL_ref`](#luaL_ref).