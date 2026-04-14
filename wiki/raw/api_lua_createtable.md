# lua_createtable

**Category**: API

### `lua_createtable`[-0, +1, *m*]

```lua
void lua_createtable (lua_State *L, int nseq, int nrec);
```

Creates a new empty table and pushes it onto the stack. Parameter `nseq` is a hint for how many elements the table will have as a sequence; parameter `nrec` is a hint for how many other elements the table will have. Lua may use these hints to preallocate memory for the new table. This preallocation may help performance when you know in advance how many elements the table will have. Otherwise you should use the function [`lua_newtable`](#lua_newtable).