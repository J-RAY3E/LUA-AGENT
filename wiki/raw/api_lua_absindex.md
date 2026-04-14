# lua_absindex

**Category**: API

### `lua_absindex`[-0, +0, –]

```lua
int lua_absindex (lua_State *L, int idx);
```

Converts the acceptable index `idx` into an equivalent absolute index (that is, one that does not depend on the stack size).