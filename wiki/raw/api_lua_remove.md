# lua_remove

**Category**: API

### `lua_remove`[-1, +0, –]

```lua
void lua_remove (lua_State *L, int index);
```

Removes the element at the given valid index, shifting down the elements above this index to fill the gap. This function cannot be called with a pseudo-index, because a pseudo-index is not an actual stack position.