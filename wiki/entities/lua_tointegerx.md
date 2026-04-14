---
title: lua_tointegerx
category: entities
created: 2026-04-14T13:49:43.991699+00:00
status: published
---

# lua_tointegerx

**Type**: Function  
**Module**: [[lua]]  

## Signature
```lua
lua_Integer lua_tointegerx (lua_State *L, int index, int *isnum)
```

## Description
Converts the Lua value at the given index to the signed integral type `lua_Integer`. The Lua value must be an integer, or a number or string convertible to an integer (see §3.4.3); otherwise, `lua_tointegerx` returns 0.

## Parameters
- `L` (lua_State*): The Lua state to operate on.
- `index` (int): The index of the Lua value to convert.
- `isnum` (int*): A pointer to a boolean value that is set to true if the operation succeeded.

## Returns
- (lua_Integer): The converted value as an integer.

## Implementation Code
```c
lua_Integer lua_tointegerx (lua_State *L, int index, int *isnum)
```
