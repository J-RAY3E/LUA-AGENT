---
title: lua_geti
category: entities
created: 2026-04-14T10:52:43.602911+00:00
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
- `L` (lua_State*): The Lua state to operate on.
- `index` (int): The index of the table or array to get the value from.
- `i` (lua_Integer): The index of the element within the table or array.

## Returns
- (int): The type of the pushed value.

## Implementation Code
```c
int lua_geti (lua_State *L, int index, lua_Integer i);
```
