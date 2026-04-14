---
title: luaL_checktype
category: entities
created: 2026-04-14T16:45:46.388775+00:00
status: draft
---

# luaL_checktype

**Type**: Function  
**Module**: [[Auxiliary Library]]  

## Signature
```lua
void luaL_checktype (lua_State *L, int arg, int t);
```

## Description
Checks whether the function argument `arg` has type `t`. See [`lua_type`](#lua_type) for the encoding of types for `t`.

## Parameters
_None_

## Returns
_None_

## Implementation Code
```c
void luaL_checktype (lua_State *L, int arg, int t);
```
