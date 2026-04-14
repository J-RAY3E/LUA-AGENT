---
title: luaL_checklstring
category: entities
created: 2026-04-14T16:44:34.440225+00:00
status: draft
---

# luaL_checklstring

**Type**: Function  
**Module**: [[auxiliary library]]  

## Signature
```lua
const char *luaL_checklstring (lua_State *L, int arg, size_t *l)
```

## Description
Checks whether the function argument `arg` is a string and returns this string; if `l` is not `NULL` fills its referent with the string's length.

## Parameters
- `L` (lua_State*): The Lua state to check the argument against.
- `arg` (int): The argument to check.
- `l` (size_t*): A pointer to a variable that will be filled with the string's length if `l` is not `NULL`.

## Returns
- (const char*): The string if `arg` is a string, or `NULL` if not.

## Implementation Code
```c
const char *luaL_checklstring (lua_State *L, int arg, size_t *l)
```
