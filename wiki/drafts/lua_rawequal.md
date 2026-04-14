---
title: lua_rawequal
category: entities
created: 2026-04-14T13:44:10.939343+00:00
status: draft
---

# lua_rawequal

**Type**: Function  
**Module**: [[lua]]  

## Signature
```lua
int lua_rawequal (lua_State *L, int index1, int index2)
```

## Description
Returns 1 if the two values in indices `index1` and `index2` are primitively equal (that is, equal without calling the `__eq` metamethod). Otherwise returns 0. Also returns 0 if any of the indices are not valid.

## Parameters
_None_

## Returns
- (int): Returns 1 if the two values in indices `index1` and `index2` are primitively equal (that is, equal without calling the `__eq` metamethod). Otherwise returns 0. Also returns 0 if any of the indices are not valid.

## Implementation Code
```c
int lua_rawequal (lua_State *L, int index1, int index2)
```
