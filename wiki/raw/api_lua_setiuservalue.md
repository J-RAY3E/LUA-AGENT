# lua_setiuservalue

**Category**: API

### `lua_setiuservalue`[-1, +0, –]

```lua
int lua_setiuservalue (lua_State *L, int index, int n);
```

Pops a value from the stack and sets it as the new `n`-th user value associated to the full userdata at the given index. Returns 0 if the userdata does not have that value.