# lua_KFunction

**Category**: API

### `lua_KFunction`

```lua
typedef int (*lua_KFunction) (lua_State *L, int status, lua_KContext ctx);
```

Type for continuation functions (see [§4.5](#4.5)).