---
title: luaL_loadfile
category: entities
created: 2026-04-14T16:48:16.431158+00:00
status: draft
---

# luaL_loadfile

**Type**: Function  
**Module**: [[auxiliary library]]  

## Signature
```lua
int luaL_loadfile (lua_State *L, const char *filename)
```

## Description
Loads a Lua file into the Lua state.

## Parameters
_None_

## Returns
- (int): Returns 0 on success, non-zero on error.

## Implementation Code
```c
int luaL_loadfile (lua_State *L, const char *filename)
```
