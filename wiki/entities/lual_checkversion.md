---
title: luaL_checkversion
category: entities
created: 2026-04-14T16:46:03.145154+00:00
status: published
---

# luaL_checkversion

**Type**: Function  
**Module**: [[auxiliary library]]  

## Signature
```lua
void luaL_checkversion (lua_State *L);
```

## Description
Checks whether the code making the call and the Lua library being called are using the same version of Lua and the same numeric types.

## Parameters
_None_

## Returns
_None_

## Implementation Code
```c
void luaL_checkversion (lua_State *L);
```
