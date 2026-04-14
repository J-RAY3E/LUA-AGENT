---
title: luaL_checkstring
category: entities
created: 2026-04-14T16:45:37.737455+00:00
status: draft
---

# luaL_checkstring

**Type**: Function  
**Module**: [[auxiliary library]]  

## Signature
```lua
const char *luaL_checkstring (lua_State *L, int arg)
```

## Description
Checks whether the function argument `arg` is a string and returns this string.

## Parameters
- `L` (lua_State*): The Lua state to check the argument against.
- `arg` (int): The argument to check.

## Returns
- (const char*): The string if `arg` is a string, otherwise `NULL`.

## Implementation Code
```c
const char *luaL_checkstring (lua_State *L, int arg)
```
