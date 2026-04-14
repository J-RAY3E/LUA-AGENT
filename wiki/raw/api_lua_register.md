# lua_register

**Category**: API

### `lua_register`[-0, +0, *e*]

```lua
void lua_register (lua_State *L, const char *name, lua_CFunction f);
```

Sets the C function `f` as the new value of global `name`. It is defined as a macro:

```lua
#define lua_register(L,n,f) \
       (lua_pushcfunction(L, f), lua_setglobal(L, n))
```