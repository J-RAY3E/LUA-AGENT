---
title: luaL_addlstring
category: entities
created: 2026-04-14T15:45:29.237383+00:00
status: published
---

# luaL_addlstring

**Type**: Function  
**Module**: [[auxiliary library]]  

## Signature
```lua
void luaL_addlstring (luaL_Buffer *B, const char *s, size_t l);
```

## Description
Adds the string pointed to by `s` with length `l` to the buffer `B` (see [`luaL_Buffer`](#luaL_Buffer)). The string can contain embedded zeros.

## Parameters
_None_

## Returns
_None_

## Implementation Code
```c
void luaL_addlstring (luaL_Buffer *B, const char *s, size_t l);
```
