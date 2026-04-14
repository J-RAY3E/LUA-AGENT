---
title: luaL_getmetafield
category: entities
created: 2026-04-14T16:47:02.612572+00:00
status: published
---

# luaL_getmetafield

**Type**: Function  
**Module**: [[Auxiliary Library]]  

## Signature
```lua
int luaL_getmetafield (lua_State *L, int obj, const char *e)
```

## Description
Pushes onto the stack the field `e` from the metatable of the object at index `obj` and returns the type of the pushed value. If the object does not have a metatable, or if the metatable does not have this field, pushes nothing and returns `LUA_TNIL`.

## Parameters
- `L` (lua_State*): The Lua state to operate on.
- `obj` (int): The index of the object in the Lua state.
- `e` (const char*): The name of the field to retrieve from the metatable.

## Returns
- (int): The type of the value pushed onto the stack.

## Implementation Code
```c
int luaL_getmetafield (lua_State *L, int obj, const char *e)
```
