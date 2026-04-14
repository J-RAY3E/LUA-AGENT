---
title: lua_pushcfunction
category: entities
created: 2026-04-14T13:42:03.477547+00:00
status: published
---

# lua_pushcfunction

**Type**: Function  
**Module**: [[lua]]  

## Signature
```lua
void lua_pushcfunction (lua_State *L, lua_CFunction f);
```

## Description
Pushes a C function onto the stack. This function is equivalent to `lua_pushcclosure` with no upvalues.

## Parameters
_None_

## Returns
_None_

## Implementation Code
```c
void lua_pushcfunction (lua_State *L, lua_CFunction f);
```
