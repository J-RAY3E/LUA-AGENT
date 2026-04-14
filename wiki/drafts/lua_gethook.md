---
title: lua_gethook
category: entities
created: 2026-04-14T13:34:23.901614+00:00
status: draft
---

# lua_gethook

**Type**: Function  
**Module**: [[lua]]  

## Signature
```lua
lua_Hook lua_gethook (lua_State *L)
```

## Description
Returns the current hook function.

## Parameters
_None_

## Returns
- (lua_Hook): The current hook function.

## Implementation Code
```c
lua_Hook lua_gethook (lua_State *L);
```
