---
title: lua_isnoneornil
category: entities
created: 2026-04-14T13:38:05.113627+00:00
status: published
---

# lua_isnoneornil

**Type**: Function  
**Module**: [[lua]]  

## Signature
```lua
int lua_isnoneornil (lua_State *L, int index)
```

## Description
Returns 1 if the given index is not valid or if the value at this index is nil, and 0 otherwise.

## Parameters
_None_

## Returns
- (int): 1 if the given index is not valid or if the value at this index is nil, and 0 otherwise.

## Implementation Code
```c
int lua_isnoneornil (lua_State *L, int index)
```
