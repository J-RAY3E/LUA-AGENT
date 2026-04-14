# lua_WarnFunction

**Category**: API

### `lua_WarnFunction`

```lua
typedef void (*lua_WarnFunction) (void *ud, const char *msg, int tocont);
```

The type of warning functions, called by Lua to emit warnings. The first parameter is an opaque pointer set by [`lua_setwarnf`](#lua_setwarnf). The second parameter is the warning message. The third parameter is a boolean that indicates whether the message is to be continued by the message in the next call.

See [`warn`](#pdf-warn) for more details about warnings.