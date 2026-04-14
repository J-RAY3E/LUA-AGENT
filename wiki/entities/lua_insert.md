---
title: lua_insert
category: entities
created: 2026-04-14T13:36:40.624999+00:00
status: published
---

# lua_insert

**Type**: Function  
**Module**: [[lua]]  

## Signature
```lua
void lua_insert (lua_State *L, int index)
```

## Description
Moves the top element into the given valid index, shifting up the elements above this index to open space. This function cannot be called with a pseudo-index, because a pseudo-index is not an actual stack position.

## Parameters
_None_

## Returns
_None_

## Implementation Code
```c
void lua_insert (lua_State *L, int index)
```
