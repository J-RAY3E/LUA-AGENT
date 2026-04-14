---
title: lua_pushthread
category: entities
created: 2026-04-14T13:43:41.537300+00:00
status: draft
---

# lua_pushthread

**Type**: Function  
**Module**: [[lua]]  

## Signature
```lua
int lua_pushthread (lua_State *L);
```

## Description
Pushes the thread represented by `L` onto the stack. Returns 1 if this thread is the main thread of its state.

## Parameters
_None_

## Returns
- (int): Returns 1 if this thread is the main thread of its state.

## Implementation Code
```c
int lua_pushthread (lua_State *L);
```
