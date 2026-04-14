# lua_upvaluejoin

**Category**: API

### `lua_upvaluejoin`[-0, +0, –]

```lua
void lua_upvaluejoin (lua_State *L, int funcindex1, int n1,
                                    int funcindex2, int n2);
```

Make the `n1`-th upvalue of the Lua closure at index `funcindex1` refer to the `n2`-th upvalue of the Lua closure at index `funcindex2`.