# lua_xmove

**Category**: API

### `lua_xmove`[-?, +?, –]

```lua
void lua_xmove (lua_State *from, lua_State *to, int n);
```

Exchange values between different threads of the same state.

This function pops `n` values from the stack `from`, and pushes them onto the stack `to`.