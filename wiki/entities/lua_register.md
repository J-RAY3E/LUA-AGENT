---
title: lua_register
category: entities
created: 2026-04-14T13:45:41.054363+00:00
status: published
---

# lua_register

**Type**: Function  
**Module**: [[lua]]  

## Signature
```lua
void lua_register(lua_State *L, const char *name, lua_CFunction f)
```

## Description
Sets the C function `f` as the new value of global `name`.

## Parameters
_None_

## Returns
_None_

## Implementation Code
```c
void lua_register(lua_State *L, const char *name, lua_CFunction f)
```
