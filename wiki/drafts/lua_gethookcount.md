---
title: lua_gethookcount
category: entities
created: 2026-04-14T13:34:31.661565+00:00
status: draft
---

# lua_gethookcount

**Type**: Function  
**Module**: [[lua]]  

## Signature
```lua
int lua_gethookcount (lua_State *L)
```

## Description
Returns the current hook count.

## Parameters
_None_

## Returns
- (int): The current hook count.

## Implementation Code
```c
int lua_gethookcount (lua_State *L);
```
