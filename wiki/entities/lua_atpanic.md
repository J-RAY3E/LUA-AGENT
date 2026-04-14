---
title: lua_atpanic
category: entities
created: 2026-04-14T10:36:49.019611+00:00
status: published
---

# lua_atpanic

**Type**: Function  
**Module**: [[lua]]  

## Signature
```lua
lua_CFunction lua_atpanic (lua_State *L, lua_CFunction panicf)
```

## Description
Sets a new panic function and returns the old one (see §4.4).

## Parameters
_None_

## Returns
- (lua_CFunction): The old panic function.

## Implementation Code
```c
lua_CFunction lua_atpanic (lua_State *L, lua_CFunction panicf)
```
