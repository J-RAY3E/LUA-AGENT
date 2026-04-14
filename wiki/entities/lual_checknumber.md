---
title: luaL_checknumber
category: entities
created: 2026-04-14T16:44:53.906271+00:00
status: published
---

# luaL_checknumber

**Type**: Function  
**Module**: [[auxiliary library]]  

## Signature
```lua
lua_Number luaL_checknumber (lua_State *L, int arg)
```

## Description
Checks whether the function argument `arg` is a number and returns this number converted to a `lua_Number`.

## Parameters
_None_

## Returns
- (lua_Number): The number converted to a `lua_Number`.

## Implementation Code
```c
lua_Number luaL_checknumber (lua_State *L, int arg)
```
