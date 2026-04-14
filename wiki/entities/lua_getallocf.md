---
title: lua_getallocf
category: entities
created: 2026-04-14T13:33:48.785310+00:00
status: published
---

# lua_getallocf

**Type**: Function  
**Module**: [[lua]]  

## Signature
```lua
lua_Alloc lua_getallocf (lua_State *L, void **ud)
```

## Description
Returns the memory-allocator function of a given state. If `ud` is not `NULL`, Lua stores in `*ud` the opaque pointer given when the memory-allocator function was set.

## Parameters
_None_

## Returns
- (lua_Alloc): The memory-allocator function of the given state.

## Implementation Code
```c
lua_Alloc lua_getallocf (lua_State *L, void **ud)
```
