---
title: lua_newstate
category: entities
created: 2026-04-14T14:49:05.685354+00:00
status: draft
---

# lua_newstate

**Type**: Function  
**Module**: [[lua]]  

## Signature
```lua
lua_State* (*lua_newstate)(lua_Alloc)
```

## Description
Creates a new Lua state.

## Parameters
_None_

## Returns
- (lua_State*): A new Lua state.

## Implementation Code
```c
lua_Alloc, lua_State, lua_Number, etc.
```
