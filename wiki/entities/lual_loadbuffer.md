---
title: luaL_loadbuffer
category: entities
created: 2026-04-14T16:47:51.045373+00:00
status: published
---

# luaL_loadbuffer

**Type**: Function  
**Module**: [[Auxiliary Library]]  

## Signature
```lua
int luaL_loadbuffer (lua_State *L, const char *buff, size_t sz, const char *name)
```

## Description
Loads a buffer into the Lua state.

## Parameters
_None_

## Returns
- (int): Returns 0 on success, or a non-zero error code on failure.

## Implementation Code
```c
int luaL_loadbuffer (lua_State *L, const char *buff, size_t sz, const char *name)
```
