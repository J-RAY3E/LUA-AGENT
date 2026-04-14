# lua_next

**Category**: API

### `lua_next`[-1, +(2|0), *v*]

```lua
int lua_next (lua_State *L, int index);
```

Pops a key from the stack, and pushes a key–value pair from the table at the given index, the "next" pair after the given key. If there are no more elements in the table, then [`lua_next`](#lua_next) returns 0 and pushes nothing.

A typical table traversal looks like this:

```lua
/* table is in the stack at index 't' */
lua_pushnil(L);  /* first key */
while (lua_next(L, t) != 0) {
  /* uses 'key' (at index -2) and 'value' (at index -1) */
  printf("%s - %s\n",
         lua_typename(L, lua_type(L, -2)),
         lua_typename(L, lua_type(L, -1)));
  /* removes 'value'; keeps 'key' for next iteration */
  lua_pop(L, 1);
}
```

While traversing a table, avoid calling [`lua_tolstring`](#lua_tolstring) directly on a key, unless you know that the key is actually a string. Recall that [`lua_tolstring`](#lua_tolstring) may change the value at the given index; this confuses the next call to [`lua_next`](#lua_next).

This function may raise an error if the given key is neither **nil** nor present in the table. See function [`next`](#pdf-next) for the caveats of modifying the table during its traversal.