---
title: luaL_unref
category: entities
created: 2026-04-14T17:12:07.840545+00:00
status: published
---

# luaL_unref

**Type**: Function  
**Module**: [[auxiliary library]]  

## Signature
```lua
void luaL_unref (lua_State *L, int t, int ref)
```

## Description
Releases a reference (see `luaL_ref`).

## Parameters
_None_

## Returns
_None_

## Implementation Code
```c
void luaL_unref (lua_State *L, int t, int ref);
```
