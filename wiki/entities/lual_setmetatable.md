---
title: luaL_setmetatable
category: entities
created: 2026-04-14T17:10:57.091981+00:00
status: published
---

# luaL_setmetatable

**Type**: Function  
**Module**: [[auxiliary library]]  

## Signature
```lua
void luaL_setmetatable (lua_State *L, const char *tname);
```

## Description
Sets the metatable of the object on the top of the stack as the metatable associated with name `tname` in the registry (see [`luaL_newmetatable`](#luaL_newmetatable)).

## Parameters
_None_

## Returns
_None_

## Implementation Code
```c
void luaL_setmetatable (lua_State *L, const char *tname);
```
