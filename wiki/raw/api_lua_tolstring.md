# lua_tolstring

**Category**: API

### `lua_tolstring`[-0, +0, *m*]

```lua
const char *lua_tolstring (lua_State *L, int index, size_t *len);
```

Converts the Lua value at the given index to a C string. The Lua value must be a string or a number; otherwise, the function returns `NULL`. If the value is a number, then `lua_tolstring` also *changes the actual value in the stack to a string*. (This change confuses [`lua_next`](#lua_next) when `lua_tolstring` is applied to keys during a table traversal.)

If `len` is not `NULL`, the function sets `*len` with the string length. The returned C string always has a zero ('`\0`') after its last character, but can contain other zeros in its body.

The pointer returned by `lua_tolstring` may be invalidated by the garbage collector if the corresponding Lua value is removed from the stack (see [§4.1.3](#4.1.3)).

This function can raise memory errors only when converting a number to a string (as then it may create a new string).