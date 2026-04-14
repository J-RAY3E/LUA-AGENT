---
title: lua_isinteger
category: entities
created: 2026-04-14T13:37:28.696837+00:00
status: published
---

# lua_isinteger

**Type**: Function  
**Module**: [[lua]]  

## Signature
```lua
int lua_isinteger (lua_State *L, int index)
```

## Description
Returns 1 if the value at the given index is an integer (that is, the value is a number and is represented as an integer), and 0 otherwise.

## Parameters
- `L` (lua_State*): The Lua state to operate on.
- `index` (int): The index of the value to check.

## Returns
- (int): 1 if the value is an integer, 0 otherwise.

## Implementation Code
```c
int lua_isinteger (lua_State *L, int index)
```
