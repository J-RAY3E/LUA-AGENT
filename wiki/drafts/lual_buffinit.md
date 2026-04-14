---
title: luaL_buffinit
category: entities
created: 2026-04-14T16:42:59.886077+00:00
status: draft
---

# luaL_buffinit

**Type**: Function  
**Module**: [[auxiliary library]]  

## Signature
```lua
void luaL_buffinit (lua_State *L, luaL_Buffer *B)
```

## Description
Initializes a buffer (see `luaL_Buffer`). This function does not allocate any space; the buffer must be declared as a variable.

## Parameters
_None_

## Returns
_None_

## Implementation Code
```c
void luaL_buffinit (lua_State *L, luaL_Buffer *B)
```
