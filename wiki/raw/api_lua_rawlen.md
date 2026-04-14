# lua_rawlen

**Category**: API

### `lua_rawlen`[-0, +0, –]

```lua
lua_Unsigned lua_rawlen (lua_State *L, int index);
```

Returns the raw "length" of the value at the given index: for strings, this is the string length; for tables, this is the result of the length operator ('`#`') with no metamethods; for userdata, this is the size of the block of memory allocated for the userdata. For other values, this call returns 0.