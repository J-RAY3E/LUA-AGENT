# lua_rotate

**Category**: API

### `lua_rotate`[-0, +0, –]

```lua
void lua_rotate (lua_State *L, int idx, int n);
```

Rotates the stack elements between the valid index `idx` and the top of the stack. The elements are rotated `n` positions in the direction of the top, for a positive `n`, or `-n` positions in the direction of the bottom, for a negative `n`. The absolute value of `n` must not be greater than the size of the slice being rotated. This function cannot be called with a pseudo-index, because a pseudo-index is not an actual stack position.