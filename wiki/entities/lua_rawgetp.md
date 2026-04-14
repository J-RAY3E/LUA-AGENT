---
title: lua_rawgetp
category: entities
created: 2026-04-14T13:44:43.454516+00:00
status: published
---

# lua_rawgetp

**Type**: Function  
**Module**: [[lua]]  

## Signature
```lua
int lua_rawgetp (lua_State *L, int index, const void *p)
```

## Description
Pushes onto the stack the value `t[k]`, where `t` is the table at the given index and `k` is the pointer `p` represented as a light userdata. The access is raw; that is, it does not use the `__index` metavalue.

## Parameters
- `L` (lua_State *): The Lua state to operate on.
- `index` (int): The index of the table to access.
- `p` (const void *): The pointer to the table.

## Returns
- (int): The type of the pushed value.

## Implementation Code
```c
int lua_rawgetp (lua_State *L, int index, const void *p)
```
