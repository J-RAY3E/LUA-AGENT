---
title: lua_error
category: entities
created: 2026-04-14T13:33:24.374878+00:00
status: draft
---

# lua_error

**Type**: Function  
**Module**: [[lua]]  

## Signature
```lua
int lua_error (lua_State *L)
```

## Description
Raises a Lua error, using the value on the top of the stack as the error object. This function does a long jump, and therefore never returns (see `luaL_error`).

## Parameters
_None_

## Returns
_None_

## Implementation Code
```c
int lua_error (lua_State *L);
```
