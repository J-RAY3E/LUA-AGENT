---
title: lua_pushinteger
category: entities
created: 2026-04-14T13:42:39.805409+00:00
status: draft
---

# lua_pushinteger

**Type**: Function  
**Module**: [[lua]]  

## Signature
```lua
void lua_pushinteger (lua_State *L, lua_Integer n);
```

## Description
Pushes an integer with value `n` onto the stack.

## Parameters
_None_

## Returns
_None_

## Implementation Code
```c
void lua_pushinteger (lua_State *L, lua_Integer n);
```
