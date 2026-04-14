---
title: luaL_loadfilex
category: entities
created: 2026-04-14T16:48:27.305669+00:00
status: draft
---

# luaL_loadfilex

**Type**: Function  
**Module**: [[auxiliary library]]  

## Signature
```lua
int luaL_loadfilex (lua_State *L, const char *filename, const char *mode)
```

## Description
Loads a file as a Lua chunk. This function uses `lua_load` to load the chunk in the file named `filename`. If `filename` is `NULL`, then it loads from the standard input. The first line in the file is ignored if it starts with a `#`. The string `mode` works as in the function `lua_load`. This function returns the same results as `lua_load`, or `LUA_ERRFILE` for file-related errors.

## Parameters
_None_

## Returns
- (int): Returns the same results as `lua_load`, or `LUA_ERRFILE` for file-related errors.

## Implementation Code
```c
int luaL_loadfilex (lua_State *L, const char *filename, const char *mode)
```
