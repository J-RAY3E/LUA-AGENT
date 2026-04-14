# luaL_getmetafield

**Category**: Auxiliary Library

### `luaL_getmetafield`[-0, +(0|1), *m*]

```lua
int luaL_getmetafield (lua_State *L, int obj, const char *e);
```

Pushes onto the stack the field `e` from the metatable of the object at index `obj` and returns the type of the pushed value. If the object does not have a metatable, or if the metatable does not have this field, pushes nothing and returns `LUA_TNIL`.