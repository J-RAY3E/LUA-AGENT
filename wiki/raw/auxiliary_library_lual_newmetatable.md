# luaL_newmetatable

**Category**: Auxiliary Library

### `luaL_newmetatable`[-0, +1, *m*]

```lua
int luaL_newmetatable (lua_State *L, const char *tname);
```

If the registry already has the key `tname`, returns 0. Otherwise, creates a new table to be used as a metatable for userdata, adds to this new table the pair `__name = tname`, adds to the registry the pair `[tname] = new table`, and returns 1.

In both cases, the function pushes onto the stack the final value associated with `tname` in the registry.