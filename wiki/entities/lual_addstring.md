---
title: luaL_addstring
category: entities
created: 2026-04-14T15:45:44.197629+00:00
status: published
---

# luaL_addstring

**Type**: Function  
**Module**: [[auxiliary library]]  

## Signature
```lua
void luaL_addstring (luaL_Buffer *B, const char *s);
```

## Description
Adds the zero-terminated string pointed to by `s` to the buffer `B` (see [`luaL_Buffer`](#luaL_Buffer)).

## Parameters
_None_

## Returns
_None_

## Implementation Code
```c
void luaL_addstring (luaL_Buffer *B, const char *s);
```
