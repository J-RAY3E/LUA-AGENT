---
title: lua_compare
category: entities
created: 2026-04-14T13:32:14.677862+00:00
status: published
---

# lua_compare

**Type**: Function  
**Module**: [[lua]]  

## Signature
```lua
int lua_compare (lua_State *L, int index1, int index2, int op)
```

## Description
Compares two Lua values. Returns 1 if the value at index `index1` satisfies `op` when compared with the value at index `index2`, following the semantics of the corresponding Lua operator (that is, it may call metamethods). Otherwise returns 0. Also returns 0 if any of the indices is not valid.

## Parameters
- `index1` (int): First index to compare
- `index2` (int): Second index to compare
- `op` (int): Comparison operator

## Returns
- (int): Comparison result

## Implementation Code
```c
int lua_compare (lua_State *L, int index1, int index2, int op)
```
