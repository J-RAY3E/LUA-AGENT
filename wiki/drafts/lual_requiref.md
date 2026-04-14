---
title: luaL_requiref
category: entities
created: 2026-04-14T17:10:37.031751+00:00
status: draft
---

# luaL_requiref

**Type**: Function  
**Module**: [[auxiliary library]]  

## Signature
```lua
void luaL_requiref (lua_State *L, const char *modname, lua_CFunction openf, int glb)
```

## Description
If `package.loaded[modname]` is not true, calls the function `openf` with the string `modname` as an argument and sets the call result to `package.loaded[modname]`, as if that function has been called through [`require`](#pdf-require). If `glb` is true, also stores the module into the global variable `modname`. Leaves a copy of the module on the stack.

## Parameters
_None_

## Returns
_None_

## Implementation Code
```c
void luaL_requiref (lua_State *L, const char *modname, lua_CFunction openf, int glb)
```
