---
title: luaL_optnumber
category: entities
created: 2026-04-14T16:50:16.076428+00:00
status: draft
---

# luaL_optnumber

**Type**: Function  
**Module**: [[Auxiliary Library]]  

## Signature
```lua
lua_Number luaL_optnumber (lua_State *L, int arg, lua_Number d)
```

## Description
Returns the number from the argument if it is a number, otherwise returns the default value.

## Parameters
- `arg` (int): The argument to check and possibly return.
- `d` (lua_Number): The default value to return if the argument is absent or nil.

## Returns
- (lua_Number): The number from the argument if it is a number, otherwise the default value.

## Implementation Code
```c
lua_Number luaL_optnumber (lua_State *L, int arg, lua_Number d)
```
