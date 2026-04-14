---
title: luaL_optstring
category: entities
created: 2026-04-14T16:50:26.609247+00:00
status: published
---

# luaL_optstring

**Type**: Function  
**Module**: [[Auxiliary Library]]  

## Signature
```lua
const char *luaL_optstring (lua_State *L, int arg, const char *d)
```

## Description
If the function argument `arg` is a string, returns this string. If this argument is absent or is **nil**, returns `d`. Otherwise, raises an error.

## Parameters
- `L` (lua_State*): lua_State*
- `arg` (int): int
- `d` (const char *): const char *

## Returns
- (const char *): const char *

## Implementation Code
```c
const char *luaL_optstring (lua_State *L, int arg, const char *d)
```
