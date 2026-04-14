---
title: lua_gettop
category: entities
created: 2026-04-14T13:36:08.667397+00:00
status: draft
---

# lua_gettop

**Type**: Function  
**Module**: [[lua]]  

## Signature
```lua
int lua_gettop (lua_State *L);
```

## Description
Returns the index of the top element in the stack. Because indices start at 1, this result is equal to the number of elements in the stack; in particular, 0 means an empty stack.

## Parameters
_None_

## Returns
- (int): The index of the top element in the stack.

## Implementation Code
```c
int lua_gettop (lua_State *L);
```
