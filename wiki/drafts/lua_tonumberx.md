---
title: lua_tonumberx
category: entities
created: 2026-04-14T13:50:18.396548+00:00
status: draft
---

# lua_tonumberx

**Type**: Function  
**Module**: [[lua]]  

## Signature
```lua
lua_Number lua_tonumberx (lua_State *L, int index, int *isnum)
```

## Description
Converts the Lua value at the given index to the C type `lua_Number` (see `lua_Number`). The Lua value must be a number or a string convertible to a number (see §3.4.3); otherwise, `lua_tonumberx` returns 0.

## Parameters
- `L` (lua_State*): The Lua state to operate on.
- `index` (int): The index of the Lua value to convert.
- `isnum` (int*): A pointer to a boolean value that is set to `true` if the operation succeeded, and `false` otherwise.

## Returns
- (lua_Number): The converted value as a `lua_Number`.

## Implementation Code
```c
lua_Number lua_tonumberx (lua_State *L, int index, int *isnum)
```
