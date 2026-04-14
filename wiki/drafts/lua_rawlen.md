---
title: lua_rawlen
category: entities
created: 2026-04-14T13:44:53.197920+00:00
status: draft
---

# lua_rawlen

**Type**: Function  
**Module**: [[lua]]  

## Signature
```lua
lua_Unsigned lua_rawlen (lua_State *L, int index)
```

## Description
Returns the raw "length" of the value at the given index: for strings, this is the string length; for tables, this is the result of the length operator ('#') with no metamethods; for userdata, this is the size of the block of memory allocated for the userdata. For other values, this call returns 0.

## Parameters
_None_

## Returns
- (lua_Unsigned): The raw length of the value at the given index.

## Implementation Code
```c
lua_Unsigned lua_rawlen (lua_State *L, int index)
```
