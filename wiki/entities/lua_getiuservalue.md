---
title: lua_getiuservalue
category: entities
created: 2026-04-14T13:35:14.892363+00:00
status: published
---

# lua_getiuservalue

**Type**: Function  
**Module**: [[lua]]  

## Signature
```lua
int lua_getiuservalue (lua_State *L, int index, int n);
```

## Description
Pushes onto the stack the n-th user value associated with the full userdata at the given index and returns the type of the pushed value.

## Parameters
- `L` (lua_State*): lua_State*
- `index` (int): index
- `n` (int): n

## Returns
- (int): LUA_TNONE

## Implementation Code
```c
int lua_getiuservalue (lua_State *L, int index, int n);
```
