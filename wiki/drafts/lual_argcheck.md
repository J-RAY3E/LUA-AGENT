---
title: luaL_argcheck
category: entities
created: 2026-04-14T16:42:00.826626+00:00
status: draft
---

# luaL_argcheck

**Type**: Function  
**Module**: [[auxiliary library]]  

## Signature
```lua
void luaL_argcheck (lua_State *L, int cond, int arg, const char *extramsg)
```

## Description
Checks whether `cond` is true. If it is not, raises an error with a standard message (see [`luaL_argerror`](#luaL_argerror)).

## Parameters
- `L` (lua_State*): The Lua state to check.
- `cond` (int): The condition to check.
- `arg` (int): The argument to check.
- `extramsg` (const char*): An extra message to include in the error.

## Returns
- (void): No return value.

## Implementation Code
```c
void luaL_argcheck (lua_State *L, int cond, int arg, const char *extramsg)
```
