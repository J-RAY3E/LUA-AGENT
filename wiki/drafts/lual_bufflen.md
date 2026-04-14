---
title: luaL_bufflen
category: entities
created: 2026-04-14T16:43:17.937351+00:00
status: draft
---

# luaL_bufflen

**Type**: Function  
**Module**: [[auxiliary library]]  

## Signature
```lua
size_t luaL_bufflen (luaL_Buffer *B)
```

## Description
Returns the length of the current content of buffer B (see [luaL_Buffer](#luaL_Buffer)).

## Parameters
_None_

## Returns
- (size_t): The length of the current content of buffer B.

## Implementation Code
```c
luaL_bufflen
```
