---
title: lua_pcall
category: entities
created: 2026-04-14T13:41:14.925952+00:00
status: draft
---

# lua_pcall

**Type**: Function  
**Module**: [[lua]]  

## Signature
```lua
int lua_pcall(lua_State *L, int nargs, int nresults, int msgh)
```

## Description
Calls a function (or a callable object) in protected mode.

## Parameters
- `L` (lua_State*): The Lua state to operate on.
- `nargs` (int): The number of arguments to pass to the function.
- `nresults` (int): The number of results to expect from the function.
- `msgh` (int): The message handler index.

## Returns
- (int): The status code of the function call.

## Implementation Code
```c
int lua_pcall (lua_State *L, int nargs, int nresults, int msgh);
```
