---
title: luaL_checkudata
category: entities
created: 2026-04-14T16:45:55.457208+00:00
status: draft
---

# luaL_checkudata

**Type**: Function  
**Module**: [[Auxiliary Library]]  

## Signature
```lua
void *luaL_checkudata (lua_State *L, int arg, const char *tname);
```

## Description
Checks whether the function argument `arg` is a userdata of the type `tname` (see [`luaL_newmetatable`](#luaL_newmetatable)) and returns the userdata's memory-block address (see [`lua_touserdata`](#lua_touserdata)).

## Parameters
_None_

## Returns
- (void *): The userdata's memory-block address.

## Implementation Code
```c
void *luaL_checkudata (lua_State *L, int arg, const char *tname);
```
