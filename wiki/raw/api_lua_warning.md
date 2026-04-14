# lua_warning

**Category**: API

### `lua_warning`[-0, +0, –]

```lua
void lua_warning (lua_State *L, const char *msg, int tocont);
```

Emits a warning with the given message. A message in a call with `tocont` true should be continued in another call to this function.

See [`warn`](#pdf-warn) for more details about warnings.