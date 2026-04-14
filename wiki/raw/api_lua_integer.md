# lua_Integer

**Category**: API

### `lua_Integer`

```lua
typedef ... lua_Integer;
```

The type of integers in Lua.

By default this type is `long long`, (usually a 64-bit two's complement integer), but that can be changed to `long` or `int` (usually a 32-bit two's complement integer). (See `LUA_INT_TYPE` in `luaconf.h`.)

Lua also defines the constants `LUA_MININTEGER` and `LUA_MAXINTEGER`, with the minimum and the maximum values that fit in this type.