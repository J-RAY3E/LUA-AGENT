# lua_rawseti

**Category**: API

### `lua_rawseti`[-1, +0, *m*]

```lua
void lua_rawseti (lua_State *L, int index, lua_Integer i);
```

Does the equivalent of `t[i] = v`, where `t` is the table at the given index and `v` is the value on the top of the stack.

This function pops the value from the stack. The assignment is raw, that is, it does not use the `__newindex` metavalue.