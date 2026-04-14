---
title: lua_isthread
category: entities
created: 2026-04-14T13:38:42.458451+00:00
status: draft
---

# lua_isthread

**Type**: Function  
**Module**: [[lua]]  

## Signature
```lua
int lua_isthread (lua_State *L, int index)
```

## Description
Returns 1 if the value at the given index is a thread, and 0 otherwise.

## Parameters
_None_

## Returns
- (int): 1 if the value at the given index is a thread, and 0 otherwise.

## Implementation Code
```c
int lua_isthread (lua_State *L, int index)
```
