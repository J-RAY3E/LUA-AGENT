---
title: luaL_prepbuffer
category: entities
created: 2026-04-14T16:50:37.666199+00:00
status: published
---

# luaL_prepbuffer

**Type**: Function  
**Module**: [[auxiliary library]]  

## Signature
```lua
char *luaL_prepbuffer (luaL_Buffer *B)
```

## Description
prepares a buffer for use in Lua

## Parameters
_None_

## Returns
- (char *): pointer to the prepared buffer

## Implementation Code
```c
char *luaL_prepbuffer (luaL_Buffer *B)
```
