# lua_type

**Category**: API

### `lua_type`[-0, +0, –]

```lua
int lua_type (lua_State *L, int index);
```

Returns the type of the value in the given valid index, or `LUA_TNONE` for a non-valid but acceptable index. The types returned by [`lua_type`](#lua_type) are coded by the following constants defined in `lua.h`: `LUA_TNIL`, `LUA_TNUMBER`, `LUA_TBOOLEAN`, `LUA_TSTRING`, `LUA_TTABLE`, `LUA_TFUNCTION`, `LUA_TUSERDATA`, `LUA_TTHREAD`, and `LUA_TLIGHTUSERDATA`.