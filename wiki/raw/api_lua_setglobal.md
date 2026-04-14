# lua_setglobal

**Category**: API

### `lua_setglobal`[-1, +0, *e*]

```lua
void lua_setglobal (lua_State *L, const char *name);
```

Pops a value from the stack and sets it as the new value of global `name`.