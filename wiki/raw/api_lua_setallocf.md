# lua_setallocf

**Category**: API

### `lua_setallocf`[-0, +0, –]

```lua
void lua_setallocf (lua_State *L, lua_Alloc f, void *ud);
```

Changes the allocator function of a given state to `f` with user data `ud`.