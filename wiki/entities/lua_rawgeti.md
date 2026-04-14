---
title: lua_rawgeti
category: entities
created: 2026-04-14T13:44:32.837868+00:00
status: published
---

# lua_rawgeti

**Type**: Function  
**Module**: [[lua]]  

## Signature
```lua
int lua_rawgeti (lua_State *L, int index, lua_Integer n);
```

## Description
Pushes onto the stack the value `t[n]`, where `t` is the table at the given index. The access is raw, that is, it does not use the `__index` metavalue.

## Parameters
- `L` (lua_State*): The Lua state to operate on.
- `index` (int): The index of the table to access.
- `n` (lua_Integer): The index of the element to retrieve from the table.

## Returns
- (int): The type of the pushed value.

## Implementation Code
```c
int lua_rawgeti (lua_State *L, int index, lua_Integer n);
```
