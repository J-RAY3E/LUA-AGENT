---
title: lua_getfield
category: entities
created: 2026-04-14T10:51:56.405105+00:00
status: draft
---

# lua_getfield

**Type**: Function  
**Module**: [[lua]]  

## Signature
```lua
int lua_getfield (lua_State *L, int index, const char *k)
```

## Description
Pushes onto the stack the value `t[k]`, where `t` is the value at the given index. As in Lua, this function may trigger a metamethod for the "index" event (see §2.4).

## Parameters
- `L` (lua_State*): The Lua state to operate on.
- `index` (int): The index of the table to get the field from.
- `k` (const char*): The name of the field to get.

## Returns
- (int): The type of the pushed value.

## Implementation Code
```c
int lua_getfield (lua_State *L, int index, const char *k)
```
