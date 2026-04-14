---
title: luaL_opt
category: entities
created: 2026-04-14T16:49:37.308110+00:00
status: published
---

# luaL_opt

**Type**: Function  
**Module**: [[auxiliary library]]  

## Signature
```lua
T luaL_opt (L, func, arg, dflt)
```

## Description
This macro is defined as follows: if the argument `arg` is nil or absent, the macro results in the default `dflt`. Otherwise, it results in the result of calling `func` with the state `L` and the argument index `arg` as arguments. Note that it evaluates the expression `dflt` only if needed.

## Parameters
_None_

## Returns
- (T): The result of calling `func` with the state `L` and the argument index `arg` as arguments.

## Implementation Code
```c
lua_isnoneornil(L,(arg)) ? (dflt) : func(L,(arg))
```
