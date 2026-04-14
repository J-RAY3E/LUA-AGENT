# lua_insert

**Category**: API

### `lua_insert`[-1, +1, –]

```lua
void lua_insert (lua_State *L, int index);
```

Moves the top element into the given valid index, shifting up the elements above this index to open space. This function cannot be called with a pseudo-index, because a pseudo-index is not an actual stack position.