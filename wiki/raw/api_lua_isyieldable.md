# lua_isyieldable

**Category**: API

### `lua_isyieldable`[-0, +0, –]

```lua
int lua_isyieldable (lua_State *L);
```

Returns 1 if the given coroutine can yield, and 0 otherwise.