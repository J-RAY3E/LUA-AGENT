---
title: luaL_addchar
category: entities
created: 2026-04-14T14:49:15.698111+00:00
status: published
---

# luaL_addchar

**Type**: Function  
**Module**: [[auxiliary library]]  

## Signature
```lua
void luaL_addchar (luaL_Buffer *B, char c)
```

## Description
Adds the byte `c` to the buffer `B` (see [luaL_Buffer](#luaL_Buffer)).

## Parameters
_None_

## Returns
_None_

## Implementation Code
```c
void luaL_addchar (luaL_Buffer *B, char c)
```
