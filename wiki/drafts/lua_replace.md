---
title: lua_replace
category: entities
created: 2026-04-14T13:45:57.882273+00:00
status: draft
---

# lua_replace

**Type**: Function  
**Module**: [[lua]]  

## Signature
```lua
void lua_replace (lua_State *L, int index)
```

## Description
Moves the top element into the given valid index without shifting any element (therefore replacing the value at that given index), and then pops the top element.

## Parameters
_None_

## Returns
_None_

## Implementation Code
```c
void lua_replace (lua_State *L, int index)
```
