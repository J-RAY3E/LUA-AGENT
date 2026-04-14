---
title: lua_topointer
category: entities
created: 2026-04-14T13:50:28.447748+00:00
status: draft
---

# lua_topointer

**Type**: Function  
**Module**: [[lua]]  

## Signature
```lua
void *lua_topointer (lua_State *L, int index)
```

## Description
Converts the value at the given index to a generic C pointer (void*). The value can be a userdata, a table, a thread, a string, or a function; otherwise, lua_topointer returns NULL. Different objects will give different pointers. There is no way to convert the pointer back to its original value.

## Parameters
_None_

## Returns
- (void *): A generic C pointer (void*).

## Implementation Code
```c
const void *lua_topointer (lua_State *L, int index);
```
