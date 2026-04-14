# lua_rawsetp

**Category**: API

### `lua_rawsetp`[-1, +0, *m*]

```lua
void lua_rawsetp (lua_State *L, int index, const void *p);
```

Does the equivalent of `t[p] = v`, where `t` is the table at the given index, `p` is encoded as a light userdata, and `v` is the value on the top of the stack.

This function pops the value from the stack. The assignment is raw, that is, it does not use the `__newindex` metavalue.