---
title: luaL_pushfail
category: entities
created: 2026-04-14T16:50:56.619984+00:00
status: published
---

# luaL_pushfail

**Type**: Function  
**Module**: [[auxiliary library]]  

## Signature
```lua
void luaL_pushfail (lua_State *L);
```

## Description
Pushes the fail value onto the stack (see §6).

## Parameters
_None_

## Returns
_None_

## Implementation Code
```c
void luaL_pushfail (lua_State *L);
```
