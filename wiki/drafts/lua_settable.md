---
title: lua_settable
category: entities
created: 2026-04-14T13:47:50.795126+00:00
status: draft
---

# lua_settable

**Type**: Function  
**Module**: [[lua]]  

## Signature
```lua
void lua_settable(lua_State *L, int index)
```

## Description
Does the equivalent to `t[k] = v`, where `t` is the value at the given index, `v` is the value on the top of the stack, and `k` is the value just below the top.

## Parameters
_None_

## Returns
_None_

## Implementation Code
```c
void lua_settable(lua_State *L, int index)
```
