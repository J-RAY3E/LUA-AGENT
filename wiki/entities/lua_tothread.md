---
title: lua_tothread
category: entities
created: 2026-04-14T13:50:47.231203+00:00
status: published
---

# lua_tothread

**Type**: Function  
**Module**: [[lua]]  

## Signature
```lua
lua_State *lua_tothread (lua_State *L, int index)
```

## Description
Converts the value at the given index to a Lua thread (represented as lua_State*). This value must be a thread; otherwise, the function returns NULL.

## Parameters
_None_

## Returns
- (lua_State*): lua_State* representing the Lua thread

## Implementation Code
```c
lua_tothread
```
