---
title: lua_yieldk
category: entities
created: 2026-04-14T13:53:13.406509+00:00
status: draft
---

# lua_yieldk

**Type**: Function  
**Module**: [[lua]]  

## Signature
```lua
int lua_yieldk (lua_State *L, int nresults, lua_KContext ctx, lua_KFunction k)
```

## Description
Yields a coroutine (thread).

## Parameters
- `L` (lua_State*): The Lua state to use.
- `nresults` (int): The number of values from the stack that will be passed as results to lua_resume.
- `ctx` (lua_KContext): The continuation context.
- `k` (lua_KFunction): The continuation function to call when the coroutine resumes.

## Returns
- (int): The return value of the continuation function.

## Implementation Code
```c
int lua_yieldk (lua_State *L, int nresults, lua_KContext ctx, lua_KFunction k)
```
