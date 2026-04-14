---
title: lua_pushvalue
category: entities
created: 2026-04-14T13:43:51.336696+00:00
status: published
---

# lua_pushvalue

**Type**: Function  
**Module**: [[lua]]  

## Signature
```lua
void lua_pushvalue (lua_State *L, int index);
```

## Description
Pushes a copy of the element at the given index onto the stack.

## Parameters
_None_

## Returns
_None_

## Implementation Code
```c
void lua_pushvalue (lua_State *L, int index);
```
