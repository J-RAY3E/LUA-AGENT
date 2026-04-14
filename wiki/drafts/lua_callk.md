---
title: lua_callk
category: entities
created: 2026-04-14T13:31:08.948355+00:00
status: draft
---

# lua_callk

**Type**: Function  
**Module**: [[lua]]  

## Signature
```lua
void lua_callk (lua_State *L, int nargs, int nresults, lua_KContext ctx, lua_KFunction k)
```

## Description
This function behaves exactly like `lua_call`, but allows the called function to yield (see §4.5).

## Parameters
_None_

## Returns
_None_

## Implementation Code
```c
void lua_callk (lua_State *L, int nargs, int nresults, lua_KContext ctx, lua_KFunction k)
```
