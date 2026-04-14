---
title: lua_gethookmask
category: entities
created: 2026-04-14T10:52:32.358374+00:00
status: draft
---

# lua_gethookmask

**Type**: Function  
**Module**: [[lua]]  

## Signature
```lua
int lua_gethookmask (lua_State *L);
```

## Description
Returns the current hook mask.

## Parameters
_None_

## Returns
- (int): The current hook mask.

## Implementation Code
```c
int lua_gethookmask (lua_State *L);
```
