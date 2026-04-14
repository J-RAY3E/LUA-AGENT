---
title: lua_tonumber
category: entities
created: 2026-04-14T13:50:06.687328+00:00
status: draft
---

# lua_tonumber

**Type**: Function  
**Module**: [[lua]]  

## Signature
```lua
lua_Number lua_tonumber (lua_State *L, int index)
```

## Description
Converts a number from a Lua table to a C number.

## Parameters
_None_

## Returns
- (lua_Number): The number converted from the Lua table.

## Implementation Code
```c
lua_Number lua_tonumber (lua_State *L, int index);
```
