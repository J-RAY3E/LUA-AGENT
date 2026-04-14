---
title: lua_remove
category: entities
created: 2026-04-14T13:45:48.846408+00:00
status: draft
---

# lua_remove

**Type**: Function  
**Module**: [[lua]]  

## Signature
```lua
void lua_remove (lua_State *L, int index)
```

## Description
Removes the element at the given valid index, shifting down the elements above this index to fill the gap. This function cannot be called with a pseudo-index, because a pseudo-index is not an actual stack position.

## Parameters
_None_

## Returns
_None_

## Implementation Code
```c
void lua_remove (lua_State *L, int index)
```
