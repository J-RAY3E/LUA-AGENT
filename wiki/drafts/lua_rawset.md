---
title: lua_rawset
category: entities
created: 2026-04-14T13:45:01.464845+00:00
status: draft
---

# lua_rawset

**Type**: Function  
**Module**: [[lua]]  

## Signature
```lua
void lua_rawset (lua_State *L, int index);
```

## Description
Similar to `lua_settable`, but does a raw assignment (i.e., without metamethods). The value at `index` must be a table.

## Parameters
_None_

## Returns
_None_

## Implementation Code
```c
void lua_rawset (lua_State *L, int index);
```
