---
title: luaL_makeseed
category: entities
created: 2026-04-14T16:48:44.422629+00:00
status: draft
---

# luaL_makeseed

**Type**: Function  
**Module**: [[auxiliary library]]  

## Signature
```lua
unsigned int luaL_makeseed (lua_State *L)
```

## Description
Returns a value with a weak attempt for randomness. The parameter L can be NULL if there is no Lua state available.

## Parameters
_None_

## Returns
- (unsigned int): Returns a value with a weak attempt for randomness.

## Implementation Code
```c
unsigned int luaL_makeseed (lua_State *L);
```
