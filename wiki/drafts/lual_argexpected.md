---
title: luaL_argexpected
category: entities
created: 2026-04-14T16:42:24.034825+00:00
status: draft
---

# luaL_argexpected

**Type**: Function  
**Module**: [[auxiliary library]]  

## Signature
```lua
void luaL_argexpected (lua_State *L, int cond, int arg, const char *tname);
```

## Description
Checks whether `cond` is true. If it is not, raises an error about the type of the argument `arg` with a standard message (see [`luaL_typeerror`](#luaL_typeerror)).

## Parameters
- `L` (lua_State*): lua_State*
- `cond` (int): cond
- `arg` (int): arg
- `tname` (const char*): tname

## Returns
- (void): void

## Implementation Code
```c
void luaL_argexpected (lua_State *L, int cond, int arg, const char *tname);
```
