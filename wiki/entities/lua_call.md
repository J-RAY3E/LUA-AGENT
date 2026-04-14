---
title: lua_call
category: entities
created: 2026-04-14T14:49:05.687628+00:00
status: published
---

# lua_call

**Type**: Function  
**Module**: [[lua]]  

## Signature
```lua
int (*lua_call)(lua_State* L, int nops, int nresults)
```

## Description
Calls a Lua function.

## Parameters
- `L` (lua_State*): The Lua state to call the function in.
- `nops` (int): The number of arguments to pass to the function.
- `nresults` (int): The number of results to expect from the function.

## Returns
- (int): The number of results returned by the function.

## Implementation Code
```c
lua_Alloc, lua_State, lua_Number, etc.
```
