---
title: luaL_dofile
category: entities
created: 2026-04-14T16:46:11.800867+00:00
status: draft
---

# luaL_dofile

**Type**: Function  
**Module**: [[auxiliary library]]  

## Signature
```lua
int luaL_dofile (lua_State *L, const char *filename)
```

## Description
Loads and runs the given file.

## Parameters
_None_

## Returns
- (int): 0 if there are no errors, 1 in case of errors.

## Implementation Code
```c
int luaL_dofile (lua_State *L, const char *filename);
```
