---
title: lua_getmetatable
category: entities
created: 2026-04-14T13:35:38.523096+00:00
status: draft
---

# lua_getmetatable

**Type**: Function  
**Module**: [[lua]]  

## Signature
```lua
int lua_getmetatable (lua_State *L, int index)
```

## Description
If the value at the given index has a metatable, the function pushes that metatable onto the stack and returns 1. Otherwise, the function returns 0 and pushes nothing on the stack.

## Parameters
- `L` (lua_State*): The Lua state to operate on.
- `index` (int): The index of the value to check for a metatable.

## Returns
- (int): 1 if the value has a metatable, 0 otherwise.

## Implementation Code
```c
int lua_getmetatable (lua_State *L, int index)
```
