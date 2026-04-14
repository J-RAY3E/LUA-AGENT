---
title: luaL_checkany
category: entities
created: 2026-04-14T16:43:46.542347+00:00
status: draft
---

# luaL_checkany

**Type**: Function  
**Module**: [[Auxiliary Library]]  

## Signature
```lua
void luaL_checkany (lua_State *L, int arg)
```

## Description
Checks whether the function has an argument of any type (including nil) at position arg.

## Parameters
_None_

## Returns
_None_

## Implementation Code
```c
void luaL_checkany (lua_State *L, int arg)
```
