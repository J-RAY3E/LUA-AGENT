---
title: lua_pushboolean
category: entities
created: 2026-04-14T13:41:42.949616+00:00
status: published
---

# lua_pushboolean

**Type**: Function  
**Module**: [[lua]]  

## Signature
```lua
void lua_pushboolean (lua_State *L, int b);
```

## Description
Pushes a boolean value with value `b` onto the stack.

## Parameters
_None_

## Returns
_None_

## Implementation Code
```c
void lua_pushboolean (lua_State *L, int b);
```
