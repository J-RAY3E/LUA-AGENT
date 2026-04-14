# lua_numbertointeger

**Category**: API

### `lua_numbertointeger`

```lua
int lua_numbertointeger (lua_Number n, lua_Integer *p);
```

Tries to convert a Lua float to a Lua integer; the float `n` must have an integral value. If that value is within the range of Lua integers, it is converted to an integer and assigned to `*p`. The macro results in a boolean indicating whether the conversion was successful. (Note that this range test can be tricky to do correctly without this macro, due to rounding.)

This macro may evaluate its arguments more than once.