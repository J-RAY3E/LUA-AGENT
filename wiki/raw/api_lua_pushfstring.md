# lua_pushfstring

**Category**: API

### `lua_pushfstring`[-0, +1, *v*]

```lua
const char *lua_pushfstring (lua_State *L, const char *fmt, ...);
```

Pushes onto the stack a formatted string and returns a pointer to this string (see [§4.1.3](#4.1.3)). The result is a copy of `fmt` with each *conversion specifier* replaced by a string representation of its respective extra argument. A conversion specifier (and its corresponding extra argument) can be '`%%`' (inserts the character '`%`'), '`%s`' (inserts a zero-terminated string, with no size restrictions), '`%f`' (inserts a [`lua_Number`](#lua_Number)), '`%I`' (inserts a [`lua_Integer`](#lua_Integer)), '`%p`' (inserts a void pointer), '`%d`' (inserts an `int`), '`%c`' (inserts an `int` as a one-byte character), and '`%U`' (inserts an `unsigned long` as a UTF-8 byte sequence).

Every occurrence of '`%`' in the string `fmt` must form a valid conversion specifier.

Besides memory allocation errors, this function may raise an error if the resulting string is too large.