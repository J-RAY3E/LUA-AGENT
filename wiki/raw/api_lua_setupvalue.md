# lua_setupvalue

**Category**: API

### `lua_setupvalue`[-(0|1), +0, –]

```lua
const char *lua_setupvalue (lua_State *L, int funcindex, int n);
```

Sets the value of a closure's upvalue. It assigns the value on the top of the stack to the upvalue and returns its name. It also pops the value from the stack.

Returns `NULL` (and pops nothing) when the index `n` is greater than the number of upvalues.

Parameters `funcindex` and `n` are as in the function [`lua_getupvalue`](#lua_getupvalue).