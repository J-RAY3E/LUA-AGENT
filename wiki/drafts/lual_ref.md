---
title: luaL_ref
category: entities
created: 2026-04-14T16:51:28.097960+00:00
status: draft
---

# luaL_ref

**Type**: Function  
**Module**: [[auxiliary]]  

## Signature
```lua
int luaL_ref (lua_State *L, int t)
```

## Description
Creates and returns a reference, in the table at index t, for the object on the top of the stack (and pops the object).

## Parameters
- `L` (lua_State*): The Lua state to operate on.
- `t` (int): The index of the table to store the reference.

## Returns
- (int): The reference number.

## Implementation Code
```c
int luaL_ref (lua_State *L, int t)
```
