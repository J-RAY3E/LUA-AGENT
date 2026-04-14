---
title: luaL_argerror
category: entities
created: 2026-04-14T16:42:12.838335+00:00
status: published
---

# luaL_argerror

**Type**: Function  
**Module**: [[Auxiliary Library]]  

## Signature
```lua
int luaL_argerror (lua_State *L, int arg, const char *extramsg)
```

## Description
Raises an error reporting a problem with argument `arg` of the C function that called it, using a standard message that includes `extramsg` as a comment.

## Parameters
- `L` (lua_State*): lua_State*
- `arg` (int): argument number
- `extramsg` (const char*): extra message

## Returns
- (int): never returns

## Implementation Code
```c
int luaL_argerror (lua_State *L, int arg, const char *extramsg)
```
