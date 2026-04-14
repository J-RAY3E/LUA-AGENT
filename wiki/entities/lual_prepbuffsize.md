---
title: luaL_prepbuffsize
category: entities
created: 2026-04-14T16:50:48.554344+00:00
status: published
---

# luaL_prepbuffsize

**Type**: Function  
**Module**: [[auxiliary library]]  

## Signature
```lua
char *luaL_prepbuffsize (luaL_Buffer *B, size_t sz)
```

## Description
Returns an address to a space of size `sz` where you can copy a string to be added to buffer `B` (see `luaL_Buffer`). After copying the string into this space you must call `luaL_addsize` with the size of the string to actually add it to the buffer.

## Parameters
_None_

## Returns
- (char *): Address to a space of size `sz` where you can copy a string to be added to buffer `B`.

## Implementation Code
```c
char *luaL_prepbuffsize (luaL_Buffer *B, size_t sz)
```
