---
title: luaL_addsize
category: entities
created: 2026-04-14T15:45:36.655048+00:00
status: draft
---

# luaL_addsize

**Type**: Function  
**Module**: [[auxiliary library]]  

## Signature
```lua
void luaL_addsize (luaL_Buffer *B, size_t n)
```

## Description
Adds to the buffer B a string of length n previously copied to the buffer area (see [luaL_prepbuffer](#luaL_prepbuffer)).

## Parameters
_None_

## Returns
_None_

## Implementation Code
```c
void luaL_addsize (luaL_Buffer *B, size_t n)
```
