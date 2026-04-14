---
title: lua_checkstack
category: entities
created: 2026-04-14T10:49:07.303247+00:00
status: draft
---

# lua_checkstack

**Type**: Function  
**Module**: [[lua]]  

## Signature
```lua
int lua_checkstack (lua_State *L, int n)
```

## Description
Ensures that the stack has space for at least `n` extra elements, that is, that you can safely push up to `n` values into it. It returns false if it cannot fulfill the request, either because it would cause the stack to be greater than a fixed maximum size (typically at least several thousand elements) or because it cannot allocate memory for the extra space. This function never shrinks the stack; if the stack already has space for the extra elements, it is left unchanged.

## Parameters
_None_

## Returns
- (int): Returns false if it cannot fulfill the request.

## Implementation Code
```c
int lua_checkstack (lua_State *L, int n)
```
