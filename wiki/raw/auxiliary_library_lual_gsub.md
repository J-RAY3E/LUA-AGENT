# luaL_gsub

**Category**: Auxiliary Library

### `luaL_gsub`[-0, +1, *m*]

```lua
const char *luaL_gsub (lua_State *L,
                       const char *s,
                       const char *p,
                       const char *r);
```

Creates a copy of string `s`, replacing any occurrence of the string `p` with the string `r`. Pushes the resulting string on the stack and returns it.