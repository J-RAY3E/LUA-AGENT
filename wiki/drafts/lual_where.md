---
title: luaL_where
category: entities
created: 2026-04-14T17:12:19.781875+00:00
status: draft
---

# luaL_where

**Type**: Function  
**Module**: [[auxiliary library]]  

## Signature
```lua
void luaL_where (lua_State *L, int lvl)
```

## Description
Pushes onto the stack a string identifying the current position of the control at level `lvl` in the call stack. Typically this string has the following format: `chunkname:currentline:`. Level 0 is the running function, level 1 is the function that called the running function, etc.

## Parameters
- `L` (lua_State*): The Lua state to operate on.
- `lvl` (int): The level of the current call stack.

## Returns
- (void): No return value.

## Implementation Code
```c
void luaL_where (lua_State *L, int lvl)
```
