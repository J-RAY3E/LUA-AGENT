---
title: lua_newtable
category: entities
created: 2026-04-14T13:39:57.146829+00:00
status: published
---

# lua_newtable

**Type**: Function  
**Module**: [[lua]]  

## Signature
```lua
void lua_newtable (lua_State *L);
```

## Description
Creates a new empty table and pushes it onto the stack. It is equivalent to `lua_createtable(L,0,0).'

## Parameters
_None_

## Returns
_None_

## Implementation Code
```c
void lua_newtable (lua_State *L);
```
