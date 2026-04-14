---
title: luaL_buffaddr
category: entities
created: 2026-04-14T16:42:32.726067+00:00
status: draft
---

# luaL_buffaddr

**Type**: Function  
**Module**: [[auxiliary library]]  

## Signature
```lua
char *luaL_buffaddr (luaL_Buffer *B)
```

## Description
Returns the address of the current content of buffer B (see `luaL_Buffer`). Note that any addition to the buffer may invalidate this address.

## Parameters
_None_

## Returns
- (char *): Address of the current content of buffer B

## Implementation Code
```c
char *luaL_buffaddr (luaL_Buffer *B)
```
