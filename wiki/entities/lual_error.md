---
title: luaL_error
category: entities
created: 2026-04-14T16:46:31.028557+00:00
status: published
---

# luaL_error

**Type**: Function  
**Module**: [[auxiliary library]]  

## Signature
```lua
int luaL_error (lua_State *L, const char *fmt, ...)
```

## Description
Raises an error. The error message format is given by `fmt` plus any extra arguments, following the same rules of `lua_pushfstring`. It also adds at the beginning of the message the file name and the line number where the error occurred, if this information is available.

## Parameters
_None_

## Returns
_None_

## Implementation Code
```c
int luaL_error (lua_State *L, const char *fmt, ...) { /* implementation details */ return 0; }
```
