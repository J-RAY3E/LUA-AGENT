---
title: lua_newuserdatauv
category: entities
created: 2026-04-14T13:40:15.991573+00:00
status: draft
---

# lua_newuserdatauv

**Type**: Function  
**Module**: [[lua]]  

## Signature
```lua
void *lua_newuserdatauv (lua_State *L, size_t size, int nuvalue);
```

## Description
Creates and pushes on the stack a new full userdata with associated Lua values and raw memory.

## Parameters
_None_

## Returns
- (void *): Address of the block of memory.

## Implementation Code
```c
void *lua_newuserdatauv (lua_State *L, size_t size, int nuvalue);
```
