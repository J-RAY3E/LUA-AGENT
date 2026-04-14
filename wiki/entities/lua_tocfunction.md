---
title: lua_tocfunction
category: entities
created: 2026-04-14T13:49:14.718245+00:00
status: published
---

# lua_tocfunction

**Type**: Function  
**Module**: [[lua]]  

## Signature
```lua
lua_CFunction lua_tocfunction (lua_State *L, int index);
```

## Description
Converts a value at the given index to a C function. That value must be a C function; otherwise, returns NULL.

## Parameters
_None_

## Returns
- (lua_CFunction): Converted C function

## Implementation Code
```c
lua_CFunction lua_tocfunction (lua_State *L, int index);
```
