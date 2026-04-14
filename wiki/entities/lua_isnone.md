---
title: lua_isnone
category: entities
created: 2026-04-14T13:37:54.342983+00:00
status: published
---

# lua_isnone

**Type**: Function  
**Module**: [[lua]]  

## Signature
```lua
int lua_isnone (lua_State *L, int index)
```

## Description
Returns 1 if the given index is not valid, and 0 otherwise.

## Parameters
_None_

## Returns
- (int): 1 if the given index is not valid, and 0 otherwise.

## Implementation Code
```c
int lua_isnone (lua_State *L, int index)
```
