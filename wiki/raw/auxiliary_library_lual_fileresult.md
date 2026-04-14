# luaL_fileresult

**Category**: Auxiliary Library

### `luaL_fileresult`[-0, +(1|3), *m*]

```lua
int luaL_fileresult (lua_State *L, int stat, const char *fname);
```

This function produces the return values for file-related functions in the standard library ([`io.open`](#pdf-io.open), [`os.rename`](#pdf-os.rename), [`file:seek`](#pdf-file:seek), etc.).