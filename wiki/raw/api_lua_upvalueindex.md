# lua_upvalueindex

**Category**: API

### `lua_upvalueindex`[-0, +0, –]

```lua
int lua_upvalueindex (int i);
```

Returns the pseudo-index that represents the `i`-th upvalue of the running function (see [§4.2](#4.2)). `i` must be in the range *[1,256]*.