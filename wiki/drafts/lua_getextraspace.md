---
title: lua_getextraspace
category: entities
created: 2026-04-14T10:51:44.849153+00:00
status: draft
---

# lua_getextraspace

**Type**: Function  
**Module**: [[lua]]  

## Signature
```lua
void *lua_getextraspace (lua_State *L)
```

## Description
Returns a pointer to a raw memory area associated with the given Lua state. The application can use this area for any purpose; Lua does not use it for anything.

## Parameters
_None_

## Returns
- (void *): Pointer to a raw memory area associated with the given Lua state.

## Implementation Code
```c
void *lua_getextraspace (lua_State *L);
```
