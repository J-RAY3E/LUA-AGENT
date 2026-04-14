---
title: lua_isnumber
category: entities
created: 2026-04-14T13:38:14.642460+00:00
status: draft
---

# lua_isnumber

**Type**: Function  
**Module**: [[lua]]  

## Signature
```lua
int lua_isnumber (lua_State *L, int index)
```

## Description
Returns 1 if the value at the given index is a number or a string convertible to a number, and 0 otherwise.

## Parameters
- `L` (lua_State*): The Lua state to operate on.
- `index` (int): The index of the value to check.

## Returns
- (int): 1 if the value is a number or convertible to a number, 0 otherwise.

## Implementation Code
```c
int lua_isnumber (lua_State *L, int index)
```
