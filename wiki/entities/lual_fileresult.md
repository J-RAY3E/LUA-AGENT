---
title: luaL_fileresult
category: entities
created: 2026-04-14T16:46:50.235370+00:00
status: published
---

# luaL_fileresult

**Type**: Function  
**Module**: [[auxiliary library]]  

## Signature
```lua
int luaL_fileresult (lua_State *L, int stat, const char *fname)
```

## Description
This function produces the return values for file-related functions in the standard library (e.g., `io.open`, `os.rename`, `file:seek`, etc.).

## Parameters
_None_

## Returns
- (int): The return value from the file-related function.

## Implementation Code
```c
int luaL_fileresult (lua_State *L, int stat, const char *fname)
```
