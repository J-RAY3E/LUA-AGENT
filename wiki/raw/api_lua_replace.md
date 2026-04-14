# lua_replace

**Category**: API

### `lua_replace`[-1, +0, –]

```lua
void lua_replace (lua_State *L, int index);
```

Moves the top element into the given valid index without shifting any element (therefore replacing the value at that given index), and then pops the top element.