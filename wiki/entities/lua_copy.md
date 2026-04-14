---
title: lua_copy
category: entities
created: 2026-04-14T13:32:32.041850+00:00
status: published
---

# lua_copy

**Type**: Function  
**Module**: [[lua]]  

## Signature
```lua
void lua_copy (lua_State *L, int fromidx, int toidx);
```

## Description
Copies the element at index `fromidx` into the valid index `toidx`, replacing the value at that position. Values at other positions are not affected.

## Parameters
_None_

## Returns
_None_

## Implementation Code
```c
void lua_copy (lua_State *L, int fromidx, int toidx) { /* implementation */ }
```
