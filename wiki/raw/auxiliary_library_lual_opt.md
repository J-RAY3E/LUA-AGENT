# luaL_opt

**Category**: Auxiliary Library

### `luaL_opt`[-0, +0, –]

```lua
T luaL_opt (L, func, arg, dflt);
```

This macro is defined as follows:

```lua
(lua_isnoneornil(L,(arg)) ? (dflt) : func(L,(arg)))
```

In words, if the argument `arg` is nil or absent, the macro results in the default `dflt`. Otherwise, it results in the result of calling `func` with the state `L` and the argument index `arg` as arguments. Note that it evaluates the expression `dflt` only if needed.