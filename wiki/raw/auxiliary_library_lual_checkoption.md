# luaL_checkoption

**Category**: Auxiliary Library

### `luaL_checkoption`[-0, +0, *v*]

```lua
int luaL_checkoption (lua_State *L,
                      int arg,
                      const char *def,
                      const char *const lst[]);
```

Checks whether the function argument `arg` is a string and searches for this string in the array `lst` (which must be NULL-terminated). Returns the index in the array where the string was found. Raises an error if the argument is not a string or if the string cannot be found.

If `def` is not `NULL`, the function uses `def` as a default value when there is no argument `arg` or when this argument is **nil**.

This is a useful function for mapping strings to C enums. (The usual convention in Lua libraries is to use strings instead of numbers to select options.)