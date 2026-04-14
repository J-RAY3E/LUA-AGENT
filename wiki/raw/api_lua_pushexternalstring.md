# lua_pushexternalstring

**Category**: API

### `lua_pushexternalstring`[-0, +1, *m*]

```lua
const char *lua_pushexternalstring (lua_State *L,
                const char *s, size_t len, lua_Alloc falloc, void *ud);
```

Creates an *external string*, that is, a string that uses memory not managed by Lua. The pointer `s` points to the external buffer holding the string content, and `len` is the length of the string. The string should have a zero at its end, that is, the condition `s[len] == '\0'` should hold. As with any string in Lua, the length must fit in a Lua integer.

If `falloc` is different from `NULL`, that function will be called by Lua when the external buffer is no longer needed. The contents of the buffer should not change before this call. The function will be called with the given `ud`, the string `s` as the block, the length plus one (to account for the ending zero) as the old size, and 0 as the new size.

Even when using an external buffer, Lua still has to allocate a header for the string. In case of a memory-allocation error, Lua will call `falloc` before raising the error.

The function returns a pointer to the string (that is, `s`).