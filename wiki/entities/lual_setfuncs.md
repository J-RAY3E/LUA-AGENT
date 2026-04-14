---
title: luaL_setfuncs
category: entities
created: 2026-04-14T17:10:48.730072+00:00
status: published
---

# luaL_setfuncs

**Type**: Function  
**Module**: [[Auxiliary Library]]  

## Signature
```lua
void luaL_setfuncs (lua_State *L, const luaL_Reg *l, int nup);
```

## Description
Registers all functions in the array `l` into the table on the top of the stack (below optional upvalues, see next). When `nup` is not zero, all functions are created with `nup` upvalues, initialized with copies of the `nup` values previously pushed on the stack on top of the library table. These values are popped from the stack after the registration. A function with a `NULL` value represents a placeholder, which is filled with **false**.

## Parameters
_None_

## Returns
_None_

## Implementation Code
```c
void luaL_setfuncs (lua_State *L, const luaL_Reg *l, int nup);
```
