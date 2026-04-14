---
title: luaL_callmeta
category: entities
created: 2026-04-14T16:43:38.272573+00:00
status: published
---

# luaL_callmeta

**Type**: Function  
**Module**: [[auxiliary library]]  

## Signature
```lua
int luaL_callmeta (lua_State *L, int obj, const char *e)
```

## Description
Calls a metamethod.

## Parameters
- `L` (lua_State*): The Lua state to operate on.
- `obj` (int): The index of the object to call the metamethod on.
- `e` (const char*): The metamethod name.

## Returns
- (int): Returns 1 if the metamethod was called, 0 otherwise.

## Implementation Code
```c
int luaL_callmeta (lua_State *L, int obj, const char *e)
```
