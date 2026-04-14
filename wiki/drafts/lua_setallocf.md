---
title: lua_setallocf
category: entities
created: 2026-04-14T13:46:31.383038+00:00
status: draft
---

# lua_setallocf

**Type**: Function  
**Module**: [[lua]]  

## Signature
```lua
void lua_setallocf (lua_State *L, lua_Alloc f, void *ud);
```

## Description
Changes the allocator function of a given state to `f` with user data `ud`.

## Parameters
_None_

## Returns
_None_

## Implementation Code
```c
void lua_setallocf (lua_State *L, lua_Alloc f, void *ud);
```
