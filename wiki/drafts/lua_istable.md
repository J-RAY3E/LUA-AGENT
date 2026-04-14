---
title: lua_istable
category: entities
created: 2026-04-14T13:38:32.504267+00:00
status: draft
---

# lua_istable

**Type**: Function  
**Module**: [[lua]]  

## Signature
```lua
int lua_istable (lua_State *L, int index)
```

## Description
Returns 1 if the value at the given index is a table, and 0 otherwise.

## Parameters
_None_

## Returns
- (int): 1 if the value at the given index is a table, and 0 otherwise.

## Implementation Code
```c
int lua_istable (lua_State *L, int index)
```
