---
title: luaL_newlib
category: entities
created: 2026-04-14T16:48:54.928185+00:00
status: published
---

# luaL_newlib

**Type**: Function  
**Module**: [[lua]]  

## Signature
```lua
void luaL_newlib (lua_State *L, const luaL_Reg l[])
```

## Description
Creates a new table and registers there the functions in the list `l`.

## Parameters
- `L` (lua_State*): The Lua state to operate on.
- `l` (const luaL_Reg[]): The list of functions to register.

## Returns
- (void): No return value.

## Implementation Code
```c
void luaL_newlib (lua_State *L, const luaL_Reg l[])
```
