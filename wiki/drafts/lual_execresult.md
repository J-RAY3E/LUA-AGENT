---
title: luaL_execresult
category: entities
created: 2026-04-14T16:46:39.373486+00:00
status: draft
---

# luaL_execresult

**Type**: Function  
**Module**: [[auxiliary library]]  

## Signature
```lua
int luaL_execresult (lua_State *L, int stat)
```

## Description
This function produces the return values for process-related functions in the standard library (os.execute and io.close).

## Parameters
_None_

## Returns
- (int): The return value from the process execution.

## Implementation Code
```c
int luaL_execresult (lua_State *L, int stat)
```
