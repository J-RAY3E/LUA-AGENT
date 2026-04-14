# lua_getglobal

**Category**: API

### `lua_getglobal`[-0, +1, *e*]

```lua
int lua_getglobal (lua_State *L, const char *name);
```

Pushes onto the stack the value of the global `name`. Returns the type of that value.