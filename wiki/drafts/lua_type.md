---
title: lua_type
category: entities
created: 2026-04-14T13:51:07.274579+00:00
status: draft
---

# lua_type

**Type**: Function  
**Module**: [[lua]]  

## Signature
```lua
int lua_type (lua_State *L, int index)
```

## Description
Returns the type of the value in the given valid index, or `LUA_TNONE` for a non-valid but acceptable index. The types returned by `lua_type` are coded by the following constants defined in `lua.h`: `LUA_TNIL`, `LUA_TNUMBER`, `LUA_TBOOLEAN`, `LUA_TSTRING`, `LUA_TTABLE`, `LUA_TFUNCTION`, `LUA_TUSERDATA`, `LUA_TTHREAD`, and `LUA_TLIGHTUSERDATA`. 

## Parameters
_None_

## Returns
- (int): The type of the value in the given valid index, or `LUA_TNONE` for a non-valid but acceptable index. The types returned by `lua_type` are coded by the following constants defined in `lua.h`: `LUA_TNIL`, `LUA_TNUMBER`, `LUA_TBOOLEAN`, `LUA_TSTRING`, `LUA_TTABLE`, `LUA_TFUNCTION`, `LUA_TUSERDATA`, `LUA_TTHREAD`, and `LUA_TLIGHTUSERDATA`. 

## Implementation Code
```c
int lua_type (lua_State *L, int index);
```
