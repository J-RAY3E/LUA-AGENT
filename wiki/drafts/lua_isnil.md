---
title: lua_isnil
category: entities
created: 2026-04-14T13:37:46.289345+00:00
status: draft
---

# lua_isnil

**Type**: Function  
**Module**: [[lua]]  

## Signature
```lua
int lua_isnil (lua_State *L, int index)
```

## Description
Returns 1 if the value at the given index is nil, and 0 otherwise.

## Parameters
- `L` (lua_State*): The Lua state to operate on.
- `index` (int): The index of the value to check.

## Returns
- (int): 1 if the value at the given index is nil, and 0 otherwise.

## Implementation Code
```c
int lua_isnil (lua_State *L, int index)
```
