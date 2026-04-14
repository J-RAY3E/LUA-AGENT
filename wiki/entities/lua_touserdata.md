---
title: lua_touserdata
category: entities
created: 2026-04-14T13:50:55.592371+00:00
status: published
---

# lua_touserdata

**Type**: Function  
**Module**: [[lua]]  

## Signature
```lua
void *lua_touserdata (lua_State *L, int index)
```

## Description
Returns the memory-block address of a full userdata or the value of a light userdata.

## Parameters
_None_

## Returns
- (void *): The memory-block address of a full userdata or the value of a light userdata.

## Implementation Code
```c
void *lua_touserdata (lua_State *L, int index)
```
