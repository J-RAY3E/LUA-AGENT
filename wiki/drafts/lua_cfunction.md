---
title: lua_CFunction
category: entities
created: 2026-04-14T13:31:18.565143+00:00
status: draft
---

# lua_CFunction

**Type**: Function  
**Module**: [[lua]]  

## Signature
```lua
int (*lua_CFunction)(lua_State *L)
```

## Description
Type for C functions.

## Parameters
_None_

## Returns
- (int): Number of results

## Implementation Code
```c
typedef int (*lua_CFunction)(lua_State *L);
```
