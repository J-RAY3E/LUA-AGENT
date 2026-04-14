# lua_upvalueid

**Category**: API

### `lua_upvalueid`[-0, +0, –]

```lua
void *lua_upvalueid (lua_State *L, int funcindex, int n);
```

Returns a unique identifier for the upvalue numbered `n` from the closure at index `funcindex`.

These unique identifiers allow a program to check whether different closures share upvalues. Lua closures that share an upvalue (that is, that access a same external local variable) will return identical ids for those upvalue indices.

Parameters `funcindex` and `n` are as in the function [`lua_getupvalue`](#lua_getupvalue), but `n` cannot be greater than the number of upvalues.