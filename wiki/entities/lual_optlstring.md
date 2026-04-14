---
title: luaL_optlstring
category: entities
created: 2026-04-14T16:50:04.421268+00:00
status: published
---

# luaL_optlstring

**Type**: Function  
**Module**: [[auxiliary library]]  

## Signature
```lua
const char *luaL_optlstring (lua_State *L, int arg, const char *d, size_t *l)
```

## Description
If the function argument `arg` is a string, returns this string. If this argument is absent or is `nil`, returns `d`. Otherwise, raises an error.

## Parameters
- `L` (lua_State*): Lua state
- `arg` (int): Argument index
- `d` (const char *): Default value if `arg` is absent or `nil`
- `l` (size_t*): Pointer to store the result's length

## Returns
- (const char*): Resulting string or `NULL` if `d` is `NULL` and `arg` is absent or `nil`

## Implementation Code
```c
const char *luaL_optlstring (lua_State *L, int arg, const char *d, size_t *l)
```
