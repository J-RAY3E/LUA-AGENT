---
title: lua_gettable
category: entities
created: 2026-04-14T13:36:00.041927+00:00
status: published
---

# lua_gettable

**Type**: Function  
**Module**: [[lua]]  

## Signature
```lua
int lua_gettable (lua_State *L, int index);
```

## Description
Pushes onto the stack the value `t[k]`, where `t` is the value at the given index and `k` is the value on the top of the stack.

## Parameters
- `L` (lua_State*): The Lua state to operate on.
- `index` (int): The index of the table to retrieve the value from.

## Returns
- (int): The type of the pushed value.

## Implementation Code
```c
int lua_gettable (lua_State *L, int index);
```
