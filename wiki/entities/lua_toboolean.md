---
title: lua_toboolean
category: entities
created: 2026-04-14T13:49:05.281716+00:00
status: published
---

# lua_toboolean

**Type**: Function  
**Module**: [[lua]]  

## Signature
```lua
int lua_toboolean (lua_State *L, int index)
```

## Description
Converts the Lua value at the given index to a C boolean value (0 or 1).

## Parameters
_None_

## Returns
- (int): 0 or 1

## Implementation Code
```c
int lua_toboolean (lua_State *L, int index)
```
