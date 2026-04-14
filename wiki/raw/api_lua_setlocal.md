# lua_setlocal

**Category**: API

### `lua_setlocal`[-(0|1), +0, –]

```lua
const char *lua_setlocal (lua_State *L, const lua_Debug *ar, int n);
```

Sets the value of a local variable of a given activation record. It assigns the value on the top of the stack to the variable and returns its name. It also pops the value from the stack.

Returns `NULL` (and pops nothing) when the index is greater than the number of active local variables.

Parameters `ar` and `n` are as in the function [`lua_getlocal`](#lua_getlocal).