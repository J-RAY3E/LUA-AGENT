# luaL_setfuncs

**Category**: Auxiliary Library

### `luaL_setfuncs`[-nup, +0, *m*]

```lua
void luaL_setfuncs (lua_State *L, const luaL_Reg *l, int nup);
```

Registers all functions in the array `l` (see [`luaL_Reg`](#luaL_Reg)) into the table on the top of the stack (below optional upvalues, see next).

When `nup` is not zero, all functions are created with `nup` upvalues, initialized with copies of the `nup` values previously pushed on the stack on top of the library table. These values are popped from the stack after the registration.

A function with a `NULL` value represents a placeholder, which is filled with **false**.