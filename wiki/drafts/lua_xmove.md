---
title: lua_xmove
category: entities
created: 2026-04-14T13:52:47.190027+00:00
status: draft
---

# lua_xmove

**Type**: Function  
**Module**: [[lua]]  

## Signature
```lua
void lua_xmove (lua_State *from, lua_State *to, int n);
```

## Description
Exchange values between different threads of the same state.

## Parameters
_None_

## Returns
_None_

## Implementation Code
```c
void lua_xmove (lua_State *from, lua_State *to, int n);
```
