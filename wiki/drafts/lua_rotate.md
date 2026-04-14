---
title: lua_rotate
category: entities
created: 2026-04-14T13:46:22.834422+00:00
status: draft
---

# lua_rotate

**Type**: Function  
**Module**: [[lua]]  

## Signature
```lua
void lua_rotate (lua_State *L, int idx, int n)
```

## Description
Rotates the stack elements between the valid index `idx` and the top of the stack. The elements are rotated `n` positions in the direction of the top, for a positive `n`, or `-n` positions in the direction of the bottom, for a negative `n`. The absolute value of `n` must not be greater than the size of the slice being rotated. This function cannot be called with a pseudo-index, because a pseudo-index is not an actual stack position.

## Parameters
- `L` (lua_State *): The Lua state to operate on.
- `idx` (int): The index of the element to start rotating from.
- `n` (int): The number of positions to rotate the elements.

## Returns
- (void): No return value.

## Implementation Code
```c
void lua_rotate (lua_State *L, int idx, int n)
```
