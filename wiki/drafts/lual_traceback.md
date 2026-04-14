---
title: luaL_traceback
category: entities
created: 2026-04-14T17:11:41.072084+00:00
status: draft
---

# luaL_traceback

**Type**: Function  
**Module**: [[Auxiliary Library]]  

## Signature
```lua
void luaL_traceback (lua_State *L, lua_State *L1, const char *msg, int level)
```

## Description
Creates and pushes a traceback of the stack L1. If msg is not NULL, it is appended at the beginning of the traceback. The level parameter tells at which level to start the traceback.

## Parameters
_None_

## Returns
_None_

## Implementation Code
```c
void luaL_traceback (lua_State *L, lua_State *L1, const char *msg, int level)
```
