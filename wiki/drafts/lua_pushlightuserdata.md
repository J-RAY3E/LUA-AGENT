---
title: lua_pushlightuserdata
category: entities
created: 2026-04-14T13:42:47.386539+00:00
status: draft
---

# lua_pushlightuserdata

**Type**: Function  
**Module**: [[lua]]  

## Signature
```lua
void lua_pushlightuserdata (lua_State *L, void *p);
```

## Description
Pushes a light userdata onto the stack.

## Parameters
_None_

## Returns
_None_

## Implementation Code
```c
void lua_pushlightuserdata (lua_State *L, void *p);
```
