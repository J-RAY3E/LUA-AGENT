---
title: lua_status
category: entities
created: 2026-04-14T13:48:46.629908+00:00
status: draft
---

# lua_status

**Type**: Function  
**Module**: [[lua]]  

## Signature
```lua
int lua_status (lua_State *L)
```

## Description
Returns the status of the thread L.

## Parameters
_None_

## Returns
- (int): The status of the thread L.

## Implementation Code
```c
int lua_status (lua_State *L);
```
