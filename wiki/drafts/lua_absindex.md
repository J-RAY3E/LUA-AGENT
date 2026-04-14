---
title: lua_absindex
category: entities
created: 2026-04-14T13:30:14.908625+00:00
status: draft
---

# lua_absindex

**Type**: Function  
**Module**: [[lua]]  

## Signature
```lua
int lua_absindex (lua_State *L, int idx)
```

## Description
Converts the acceptable index `idx` into an equivalent absolute index (that is, one that does not depend on the stack size).

## Parameters
_None_

## Returns
- (int): The absolute index.

## Implementation Code
```c
int lua_absindex (lua_State *L, int idx)
```
