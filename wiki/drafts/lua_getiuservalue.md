---
title: lua_getiuservalue
category: entities
created: 2026-04-14T10:53:07.632390+00:00
status: draft
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
- `L` (lua_State*): lua_State* is a pointer to a Lua state.
- `index` (int): Index of the userdata.
- `n` (int): Number of user values to push.

## Returns
- (int): Returns the type of the pushed value.

## Implementation Code
```c
int lua_getiuservalue (lua_State *L, int index, int n);
```
