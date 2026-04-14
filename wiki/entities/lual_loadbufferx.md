---
title: luaL_loadbufferx
category: entities
created: 2026-04-14T16:48:03.865349+00:00
status: published
---

# luaL_loadbufferx

**Type**: Function  
**Module**: [[auxiliary library]]  

## Signature
```lua
int luaL_loadbufferx (lua_State *L, const char *buff, size_t sz, const char *name, const char *mode)
```

## Description
Loads a buffer as a Lua chunk. This function uses `lua_load` to load the chunk in the buffer pointed to by `buff` with size `sz`.

## Parameters
- `L` (lua_State *): The Lua state to operate on.
- `buff` (const char *): The buffer containing the Lua chunk to load.
- `sz` (size_t): The size of the buffer in bytes.
- `name` (const char *): The name of the chunk to load.
- `mode` (const char *): The mode for loading the chunk.

## Returns
- (int): The result of the function call.

## Implementation Code
```c
int luaL_loadbufferx (lua_State *L, const char *buff, size_t sz, const char *name, const char *mode)
```
