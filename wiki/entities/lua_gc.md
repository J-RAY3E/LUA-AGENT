---
title: lua_gc
category: entities
created: 2026-04-14T13:33:39.885271+00:00
status: published
---

# lua_gc

**Type**: Function  
**Module**: [[lua]]  

## Signature
```lua
int lua_gc(lua_State *L, int what, ...)
```

## Description
Controls the garbage collector.

## Parameters
- `L` (lua_State*): The Lua state to operate on.
- `what` (int): The action to perform.

## Returns
- (int): The result of the operation.

## Implementation Code
```c
int lua_gc(lua_State *L, int what, ...) {
  // Function implementation
}
```
