---
title: lua_pcallk
category: entities
created: 2026-04-14T13:41:27.471344+00:00
status: published
---

# lua_pcallk

**Type**: Function  
**Module**: [[lua]]  

## Signature
```lua
int lua_pcallk (lua_State *L, int nargs, int nresults, int msgh, lua_KContext ctx, lua_KFunction k)
```

## Description
This function behaves exactly like `lua_pcall`, except that it allows the called function to yield (see §4.5).

## Parameters
- `L` (lua_State*): The Lua state to operate on.
- `nargs` (int): The number of arguments to pass to the called function.
- `nresults` (int): The number of results to expect from the called function.
- `msgh` (int): The message to pass to the called function.
- `ctx` (lua_KContext): The context to pass to the called function.
- `k` (lua_KFunction): The function to call.

## Returns
- (int): The return value of the called function.

## Implementation Code
```c
int lua_pcallk (lua_State *L, int nargs, int nresults, int msgh, lua_KContext ctx, lua_KFunction k)
```
