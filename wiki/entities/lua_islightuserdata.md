---
title: lua_islightuserdata
category: entities
created: 2026-04-14T13:37:37.142579+00:00
status: published
---

# lua_islightuserdata

**Type**: Function  
**Module**: [[lua]]  

## Signature
```lua
int lua_islightuserdata(lua_State *L, int index)
```

## Description
Returns 1 if the value at the given index is a light userdata, and 0 otherwise.

## Parameters
_None_

## Returns
- (int): 1 if the value at the given index is a light userdata, and 0 otherwise.

## Implementation Code
```c
int lua_islightuserdata(lua_State *L, int index)
```
