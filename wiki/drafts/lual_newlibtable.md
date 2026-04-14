---
title: luaL_newlibtable
category: entities
created: 2026-04-14T16:49:04.005622+00:00
status: draft
---

# luaL_newlibtable

**Type**: Function  
**Module**: [[auxiliary library]]  

## Signature
```lua
void luaL_newlibtable (lua_State *L, const luaL_Reg l[])
```

## Description
Creates a new table with a size optimized to store all entries in the array `l` (but does not actually store them). It is intended to be used in conjunction with `luaL_setfuncs` (see `luaL_newlib`).

## Parameters
_None_

## Returns
_None_

## Implementation Code
```c
void luaL_newlibtable (lua_State *L, const luaL_Reg l[])
```
