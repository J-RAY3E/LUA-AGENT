---
title: luaL_newstate
category: entities
created: 2026-04-14T16:49:25.122293+00:00
status: draft
---

# luaL_newstate

**Type**: Function  
**Module**: [[auxiliary library]]  

## Signature
```lua
lua_State *luaL_newstate (void);
```

## Description
Creates a new Lua state. It calls `lua_newstate` with `luaL_alloc` as the allocator function and the result of `luaL_makeseed(NULL)` as the seed, and then sets a warning function and a panic function (see §4.4) that print messages to the standard error output.

## Parameters
_None_

## Returns
- (lua_State *): The new state, or NULL if there is a memory allocation error.

## Implementation Code
```c
lua_State *luaL_newstate (void);
```
