---
title: luaL_buffsub
category: entities
created: 2026-04-14T16:43:26.173927+00:00
status: published
---

# luaL_buffsub

**Type**: Function  
**Module**: [[auxiliary library]]  

## Signature
```lua
void luaL_buffsub (luaL_Buffer *B, int n)
```

## Description
Removes `n` bytes from the buffer `B` (see [`luaL_Buffer`](#luaL_Buffer)). The buffer must have at least that many bytes.

## Parameters
_None_

## Returns
_None_

## Implementation Code
```c
void luaL_buffsub (luaL_Buffer *B, int n)
```
