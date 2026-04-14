---
title: luaL_typeerror
category: entities
created: 2026-04-14T17:11:51.172729+00:00
status: published
---

# luaL_typeerror

**Type**: Function  
**Module**: [[auxiliary library]]  

## Signature
```lua
int luaL_typeerror (lua_State *L, int arg, const char *tname)
```

## Description
Raises a type error for the argument `arg` of the C function that called it, using a standard message; `tname` is a 'name' for the expected type. This function never returns.

## Parameters
- `arg` (int): Argument for the C function that called it.
- `tname` (const char *): Name for the expected type.

## Returns
- (int): Not applicable.

## Implementation Code
```c
int luaL_typeerror (lua_State *L, int arg, const char *tname)
```
