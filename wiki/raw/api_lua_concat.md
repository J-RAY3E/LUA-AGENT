# lua_concat

**Category**: API

### `lua_concat`[-n, +1, *e*]

```lua
void lua_concat (lua_State *L, int n);
```

Concatenates the `n` values at the top of the stack, pops them, and leaves the result on the top. If `n` is 1, the result is the single value on the stack (that is, the function does nothing); if `n` is 0, the result is the empty string. Concatenation is performed following the usual semantics of Lua (see [§3.4.6](#3.4.6)).