---
title: lua_gc
category: entities
created: 2026-04-14T10:51:24.569125+00:00
status: draft
---

# lua_gc

**Type**: Function  
**Module**: [[lua]]  

## Signature
```lua
int lua_gc (lua_State *L, int what, ...)
```

## Description
Controls the garbage collector.

## Parameters
- `L` (lua_State*): The Lua state to operate on.
- `what` (int): The garbage collection option to perform.

## Returns
- (int): The result of the garbage collection operation.

## Implementation Code
```c
int lua_gc (lua_State *L, int what, ...) { /* implementation details */ }
```
