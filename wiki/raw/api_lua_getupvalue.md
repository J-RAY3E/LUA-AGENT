# lua_getupvalue

**Category**: API

### `lua_getupvalue`[-0, +(0|1), –]

```lua
const char *lua_getupvalue (lua_State *L, int funcindex, int n);
```

Gets information about the `n`-th upvalue of the closure at index `funcindex`. It pushes the upvalue's value onto the stack and returns its name. Returns `NULL` (and pushes nothing) when the index `n` is greater than the number of upvalues.

See [`debug.getupvalue`](#pdf-debug.getupvalue) for more information about upvalues.