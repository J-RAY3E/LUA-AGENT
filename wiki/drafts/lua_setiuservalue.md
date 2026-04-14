---
title: lua_setiuservalue
category: entities
created: 2026-04-14T13:47:21.338043+00:00
status: draft
---

# lua_setiuservalue

**Type**: Function  
**Module**: [[lua]]  

## Signature
```lua
int lua_setiuservalue (lua_State *L, int index, int n);
```

## Description
Pops a value from the stack and sets it as the new n-th user value associated to the full userdata at the given index. Returns 0 if the userdata does not have that value.

## Parameters
_None_

## Returns
- (int): Returns 0 if the userdata does not have that value.

## Implementation Code
```c
int lua_setiuservalue (lua_State *L, int index, int n);
```
