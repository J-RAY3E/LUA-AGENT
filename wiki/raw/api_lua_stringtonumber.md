# lua_stringtonumber

**Category**: API

### `lua_stringtonumber`[-0, +1, –]

```lua
size_t lua_stringtonumber (lua_State *L, const char *s);
```

Converts the zero-terminated string `s` to a number, pushes that number into the stack, and returns the total size of the string, that is, its length plus one. The conversion can result in an integer or a float, according to the lexical conventions of Lua (see [§3.1](#3.1)). The string may have leading and trailing whitespaces and a sign. If the string is not a valid numeral, returns 0 and pushes nothing. (Note that the result can be used as a boolean, true if the conversion succeeds.)