---
title: lua_upvalueid
category: entities
created: 2026-04-14T13:51:38.310010+00:00
status: draft
---

# lua_upvalueid

**Type**: Function  
**Module**: [[lua]]  

## Signature
```lua
void *lua_upvalueid (lua_State *L, int funcindex, int n)
```

## Description
Returns a unique identifier for the upvalue numbered `n` from the closure at index `funcindex`.

## Parameters
- `L` (lua_State *): The Lua state to operate on.
- `funcindex` (int): The index of the closure.
- `n` (int): The index of the upvalue.

## Returns
- (void *): A unique identifier for the upvalue.

## Implementation Code
```c
void *lua_upvalueid (lua_State *L, int funcindex, int n)
```
