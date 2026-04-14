---
title: luaL_checkstack
category: entities
created: 2026-04-14T16:45:26.798373+00:00
status: published
---

# luaL_checkstack

**Type**: Function  
**Module**: [[Auxiliary Library]]  

## Signature
```lua
void luaL_checkstack (lua_State *L, int sz, const char *msg);
```

## Description
Grows the stack size to `top + sz` elements, raising an error if the stack cannot grow to that size. `msg` is an additional text to go into the error message (or `NULL` for no additional text).

## Parameters
_None_

## Returns
_None_

## Implementation Code
```c
void luaL_checkstack (lua_State *L, int sz, const char *msg);
```
