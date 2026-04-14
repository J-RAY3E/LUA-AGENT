---
title: luaL_checkoption
category: entities
created: 2026-04-14T16:45:16.279325+00:00
status: published
---

# luaL_checkoption

**Type**: Function  
**Module**: [[Auxiliary Library]]  

## Signature
```lua
int luaL_checkoption (lua_State *L, int arg, const char *def, const char *const lst[])
```

## Description
Checks whether the function argument `arg` is a string and searches for this string in the array `lst` (which must be NULL-terminated). Returns the index in the array where the string was found. Raises an error if the argument is not a string or if the string cannot be found.

## Parameters
- `arg` (int): The function argument to check.
- `def` (const char *): The default value to use if the argument is not a string or if the string cannot be found.
- `lst` (const char *const []): The array of strings to search in, which must be NULL-terminated.

## Returns
- (int): The index in the array where the string was found. Returns -1 if the argument is not a string or if the string cannot be found.

## Implementation Code
```c
int luaL_checkoption (lua_State *L, int arg, const char *def, const char *const lst[])
```
