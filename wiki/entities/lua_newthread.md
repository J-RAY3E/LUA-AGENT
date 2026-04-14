---
title: lua_newthread
category: entities
created: 2026-04-14T13:40:05.904749+00:00
status: published
---

# lua_newthread

**Type**: Function  
**Module**: [[lua]]  

## Signature
```lua
lua_State *lua_newthread (lua_State *L);
```

## Description
Creates a new thread, pushes it on the stack, and returns a pointer to a `lua_State` that represents this new thread. The new thread returned by this function shares with the original thread its global environment, but has an independent execution stack.

## Parameters
_None_

## Returns
- (lua_State): A pointer to a `lua_State` that represents the new thread.

## Implementation Code
```c
lua_State *lua_newthread (lua_State *L);
```
