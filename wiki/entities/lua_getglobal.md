---
title: lua_getglobal
category: entities
created: 2026-04-14T13:34:16.245426+00:00
status: published
---

# lua_getglobal

**Type**: Function  
**Module**: [[lua]]  

## Signature
```lua
int lua_getglobal (lua_State *L, const char *name)
```

## Description
Pushes onto the stack the value of the global `name`. Returns the type of that value.

## Parameters
_None_

## Returns
- (int): The type of the value.

## Implementation Code
```c
int lua_getglobal (lua_State *L, const char *name)
```
