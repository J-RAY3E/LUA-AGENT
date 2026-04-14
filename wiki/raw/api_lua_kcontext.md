# lua_KContext

**Category**: API

### `lua_KContext`

```lua
typedef ... lua_KContext;
```

The type for continuation-function contexts. It must be a numeric type. This type is defined as `intptr_t` when `intptr_t` is available, so that it can store pointers too. Otherwise, it is defined as `ptrdiff_t`.