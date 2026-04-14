---
title: lua_iscfunction
category: entities
created: 2026-04-14T13:37:10.532938+00:00
status: draft
---

# lua_iscfunction

**Type**: Function  
**Module**: [[lua]]  

## Signature
```lua
int lua_iscfunction (lua_State *L, int index)
```

## Description
Returns 1 if the value at the given index is a C function, and 0 otherwise.

## Parameters
_None_

## Returns
- (int): 1 if the value at the given index is a C function, and 0 otherwise.

## Implementation Code
```c
int lua_iscfunction (lua_State *L, int index)
```
