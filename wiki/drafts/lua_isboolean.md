---
title: lua_isboolean
category: entities
created: 2026-04-14T13:37:00.322446+00:00
status: draft
---

# lua_isboolean

**Type**: Function  
**Module**: [[lua]]  

## Signature
```lua
int lua_isboolean (lua_State *L, int index)
```

## Description
Returns 1 if the value at the given index is a boolean, and 0 otherwise.

## Parameters
- `L` (lua_State*): The Lua state to operate on.
- `index` (int): The index of the value to check.

## Returns
- (int): 1 if the value at the given index is a boolean, and 0 otherwise.

## Implementation Code
```c
int lua_isboolean (lua_State *L, int index)
```
