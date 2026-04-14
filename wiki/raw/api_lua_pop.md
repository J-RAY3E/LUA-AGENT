# lua_pop

**Category**: API

### `lua_pop`[-n, +0, *e*]

```lua
void lua_pop (lua_State *L, int n);
```

Pops `n` elements from the stack. It is implemented as a macro over [`lua_settop`](#lua_settop).