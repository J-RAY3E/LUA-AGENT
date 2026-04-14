# lua_pushlightuserdata

**Category**: API

### `lua_pushlightuserdata`[-0, +1, –]

```lua
void lua_pushlightuserdata (lua_State *L, void *p);
```

Pushes a light userdata onto the stack.

Userdata represent C values in Lua. A *light userdata* represents a pointer, a `void*`. It is a value (like a number): you do not create it, it has no individual metatable, and it is not collected (as it was never created). A light userdata is equal to "any" light userdata with the same C address.