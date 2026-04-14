---
title: lua_isfunction
category: entities
created: 2026-04-14T13:37:19.266471+00:00
status: draft
---

# lua_isfunction

**Type**: Function  
**Module**: [[lua]]  

## Signature
```lua
int lua_isfunction (lua_State *L, int index)
```

## Description
Returns 1 if the value at the given index is a function (either C or Lua), and 0 otherwise.

## Parameters
_None_

## Returns
- (int): 1 if the value at the given index is a function (either C or Lua), and 0 otherwise.

## Implementation Code
```c
int lua_isfunction (lua_State *L, int index)
```
