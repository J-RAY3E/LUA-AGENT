---
title: lua_getstack
category: entities
created: 2026-04-14T13:35:48.924753+00:00
status: published
---

# lua_getstack

**Type**: Function  
**Module**: [[lua]]  

## Signature
```lua
int lua_getstack (lua_State *L, int level, lua_Debug *ar)
```

## Description
Gets information about the interpreter runtime stack.

## Parameters
- `L` (lua_State *): The Lua state to operate on.
- `level` (int): The level of the stack to get information about.
- `ar` (lua_Debug *): A structure to fill with information about the stack.

## Returns
- (int): Returns 1 if the stack information was successfully retrieved, 0 otherwise.

## Implementation Code
```c
int lua_getstack (lua_State *L, int level, lua_Debug *ar)
```
