---
title: luaL_getmetatable
category: entities
created: 2026-04-14T16:47:12.517060+00:00
status: published
---

# luaL_getmetatable

**Type**: Function  
**Module**: [[auxiliary library]]  

## Signature
```lua
int luaL_getmetatable (lua_State *L, const char *tname)
```

## Description
Pushes onto the stack the metatable associated with the name `tname` in the registry (see `luaL_newmetatable`), or **nil** if there is no metatable associated with that name. Returns the type of the pushed value.

## Parameters
_None_

## Returns
- (int): The type of the pushed value.

## Implementation Code
```c
int luaL_getmetatable (lua_State *L, const char *tname)
```
