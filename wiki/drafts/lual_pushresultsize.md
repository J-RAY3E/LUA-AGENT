---
title: luaL_pushresultsize
category: entities
created: 2026-04-14T16:51:13.620891+00:00
status: draft
---

# luaL_pushresultsize

**Type**: Function  
**Module**: [[auxiliary library]]  

## Signature
```lua
void luaL_pushresultsize (luaL_Buffer *B, size_t sz)
```

## Description
Pushes the size of the buffer `B` onto the stack.

## Parameters
_None_

## Returns
_None_

## Implementation Code
```c
void luaL_pushresultsize (luaL_Buffer *B, size_t sz)
```
