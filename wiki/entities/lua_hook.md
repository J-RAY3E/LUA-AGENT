---
title: lua_Hook
category: entities
created: 2026-04-14T13:36:31.901492+00:00
status: published
---

# lua_Hook

**Type**: Function  
**Module**: [[lua]]  

## Signature
```lua
void (*lua_Hook)(lua_State *L, lua_Debug *ar)
```

## Description
Type for debugging hook functions.

## Parameters
_None_

## Returns
_None_

## Implementation Code
```c
typedef void (*lua_Hook)(lua_State *L, lua_Debug *ar);
```
