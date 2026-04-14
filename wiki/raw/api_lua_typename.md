# lua_typename

**Category**: API

### `lua_typename`[-0, +0, –]

```lua
const char *lua_typename (lua_State *L, int tp);
```

Returns the name of the type encoded by the value `tp`, which must be one the values returned by [`lua_type`](#lua_type).