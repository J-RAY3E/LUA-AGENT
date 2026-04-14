---
title: luaL_loadstring
category: entities
created: 2026-04-14T16:48:36.102974+00:00
status: published
---

# luaL_loadstring

**Type**: Function  
**Module**: [[auxiliary library]]  

## Signature
```lua
int luaL_loadstring (lua_State *L, const char *s)
```

## Description
Loads a string as a Lua chunk. This function uses `lua_load` to load the chunk in the zero-terminated string `s`.

## Parameters
_None_

## Returns
_None_

## Implementation Code
```c
int luaL_loadstring (lua_State *L, const char *s)
```
