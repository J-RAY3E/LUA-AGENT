---
title: lua_geti
category: entities
created: 2026-04-14T13:34:51.058598+00:00
status: draft
---

# lua_geti

**Type**: Function  
**Module**: [[lua]]  

## Signature
```lua
int lua_geti (lua_State *L, int index, lua_Integer i);
```

## Description
Pushes onto the stack the value `t[i]`, where `t` is the value at the given index. As in Lua, this function may trigger a metamethod for the "index" event (see §2.4).

## Parameters
- `index` (int): The index of the value to retrieve.
- `i` (lua_Integer): The value to retrieve.

## Returns
- (int): The type of the pushed value.

## Implementation Code
```c
int lua_geti (lua_State *L, int index, lua_Integer i);
```
