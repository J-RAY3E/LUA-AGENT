---
title: luaL_getsubtable
category: entities
created: 2026-04-14T16:47:23.362982+00:00
status: published
---

# luaL_getsubtable

**Type**: Function  
**Module**: [[Auxiliary Library]]  

## Signature
```lua
int luaL_getsubtable (lua_State *L, int idx, const char *fname)
```

## Description
Ensures that the value `t[fname]`, where `t` is the value at index `idx`, is a table, and pushes that table onto the stack. Returns true if it finds a previous table there and false if it creates a new table.

## Parameters
- `L` (lua_State*): The Lua state to operate on.
- `idx` (int): The index of the table to check.
- `fname` (const char*): The name of the table to check.

## Returns
- (int): Returns true if it finds a previous table there and false if it creates a new table.

## Implementation Code
```c
int luaL_getsubtable (lua_State *L, int idx, const char *fname)
```
