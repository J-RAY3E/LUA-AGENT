---
title: lua_toclose
category: entities
created: 2026-04-14T13:49:24.422967+00:00
status: published
---

# lua_toclose

**Type**: Function  
**Module**: [[lua]]  

## Signature
```lua
void lua_toclose (lua_State *L, int index)
```

## Description
Marks the given index in the stack as a to-be-closed slot.

## Parameters
_None_

## Returns
_None_

## Implementation Code
```c
void lua_toclose (lua_State *L, int index)
```
