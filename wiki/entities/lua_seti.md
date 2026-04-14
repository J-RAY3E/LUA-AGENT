---
title: lua_seti
category: entities
created: 2026-04-14T13:47:11.600019+00:00
status: published
---

# lua_seti

**Type**: Function  
**Module**: [[lua]]  

## Signature
```lua
void lua_seti (lua_State *L, int index, lua_Integer n);
```

## Description
Does the equivalent to `t[n] = v`, where `t` is the value at the given index and `v` is the value on the top of the stack.

## Parameters
_None_

## Returns
_None_

## Implementation Code
```c
void lua_seti (lua_State *L, int index, lua_Integer n);
```
