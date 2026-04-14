---
title: lua_isuserdata
category: entities
created: 2026-04-14T13:38:51.156253+00:00
status: published
---

# lua_isuserdata

**Type**: Function  
**Module**: [[lua]]  

## Signature
```lua
int lua_isuserdata (lua_State *L, int index)
```

## Description
Returns 1 if the value at the given index is a userdata (either full or light), and 0 otherwise.

## Parameters
_None_

## Returns
- (int): 1 if the value at the given index is a userdata (either full or light), and 0 otherwise.

## Implementation Code
```c
int lua_isuserdata (lua_State *L, int index)
```
