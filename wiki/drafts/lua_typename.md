---
title: lua_typename
category: entities
created: 2026-04-14T13:51:16.448111+00:00
status: draft
---

# lua_typename

**Type**: Function  
**Module**: [[lua]]  

## Signature
```lua
const char *lua_typename (lua_State *L, int tp)
```

## Description
Returns the name of the type encoded by the value `tp`, which must be one the values returned by [`lua_type`](#lua_type).

## Parameters
_None_

## Returns
- (const char *): The name of the type encoded by the value `tp`, which must be one the values returned by [`lua_type`](#lua_type).

## Implementation Code
```c
const char *lua_typename (lua_State *L, int tp)
```
