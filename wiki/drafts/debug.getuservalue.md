---
title: debug.getuservalue
category: entities
created: 2026-04-14T20:08:51.084526+00:00
status: draft
---

# debug.getuservalue

**Type**: Function  
**Module**: [[Standard Libraries]]  

## Signature
```lua
debug.getuservalue(u, n)
```

## Description
Returns the n-th user value associated to the userdata u plus a boolean, false if the userdata does not have that value.

## Parameters
- `u` (const void *): User data to get the value from.
- `n` (int): Index of the user value to get.

## Returns
- (void): None
- (lua_Number): The value associated with the index n.
- (lua_Number): False if the userdata does not have that value.

## Implementation Code
```c
void debug_getuservalue(lua_State *L, const void *u, int n, lua_Number *value, lua_Number *boolean)
```
