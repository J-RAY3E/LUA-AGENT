---
title: xpcall
category: entities
created: 2026-04-14T17:13:16.637995+00:00
status: published
---

# xpcall

**Type**: Function  
**Module**: [[lua]]  

## Signature
```lua
lua_Alloc, lua_State, lua_Number
```

## Description
Calls a function in protected mode and returns a status code.

## Parameters
- `func` (lua_State): The function to call.
- `nargs` (lua_Number): The number of arguments to pass to the function.

## Returns
- (lua_Number): The status code of the function call.

## Implementation Code
```c
lua_pcall
```
