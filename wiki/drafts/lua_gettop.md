---
title: lua_gettop
category: entities
created: 2026-04-14T10:54:04.866581+00:00
status: draft
---

# lua_gettop

**Type**: Function  
**Module**: [[lua]]  

## Signature
```lua
int lua_gettop (lua_State *L);
```

## Description
Returns the index of the top element in the stack.

## Parameters
_None_

## Returns
- (int): The index of the top element in the stack.

## Implementation Code
```c
int lua_gettop (lua_State *L);
```
