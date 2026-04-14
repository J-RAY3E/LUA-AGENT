---
title: lua_upvaluejoin
category: entities
created: 2026-04-14T13:51:59.652720+00:00
status: published
---

# lua_upvaluejoin

**Type**: Function  
**Module**: [[lua]]  

## Signature
```lua
void lua_upvaluejoin (lua_State *L, int funcindex1, int n1, int funcindex2, int n2)
```

## Description
Make the n1-th upvalue of the Lua closure at index funcindex1 refer to the n2-th upvalue of the Lua closure at index funcindex2.

## Parameters
- `L` (lua_State*): The Lua state to operate on.
- `funcindex1` (int): The index of the first Lua closure.
- `n1` (int): The index of the upvalue to join.
- `funcindex2` (int): The index of the second Lua closure.
- `n2` (int): The index of the upvalue to join.

## Returns
- (void): No return value.

## Implementation Code
```c
void lua_upvaluejoin (lua_State *L, int funcindex1, int n1, int funcindex2, int n2)
```
