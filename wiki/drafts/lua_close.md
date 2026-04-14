---
title: lua_close
category: entities
created: 2026-04-14T13:31:41.122065+00:00
status: draft
---

# lua_close

**Type**: Function  
**Module**: [[lua]]  

## Signature
```lua
void lua_close (lua_State *L);
```

## Description
Close all active to-be-closed variables in the main thread, release all objects in the given Lua state (calling the corresponding garbage-collection metamethods, if any), and frees all dynamic memory used by this state.

## Parameters
_None_

## Returns
_None_

## Implementation Code
```c
void lua_close (lua_State *L);
```
