---
title: lua_isyieldable
category: entities
created: 2026-04-14T13:39:00.690253+00:00
status: published
---

# lua_isyieldable

**Type**: Function  
**Module**: [[lua]]  

## Signature
```lua
int lua_isyieldable (lua_State *L)
```

## Description
Returns 1 if the given coroutine can yield, and 0 otherwise.

## Parameters
_None_

## Returns
- (int): 1 if the given coroutine can yield, and 0 otherwise.

## Implementation Code
```c
int lua_isyieldable (lua_State *L);
```
