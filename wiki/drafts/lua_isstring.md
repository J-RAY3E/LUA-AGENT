---
title: lua_isstring
category: entities
created: 2026-04-14T13:38:23.194725+00:00
status: draft
---

# lua_isstring

**Type**: Function  
**Module**: [[lua]]  

## Signature
```lua
int lua_isstring (lua_State *L, int index)
```

## Description
Returns 1 if the value at the given index is a string or a number (which is always convertible to a string), and 0 otherwise.

## Parameters
_None_

## Returns
- (int): 1 if the value at the given index is a string or a number (which is always convertible to a string), and 0 otherwise.

## Implementation Code
```c
int lua_isstring (lua_State *L, int index)
```
