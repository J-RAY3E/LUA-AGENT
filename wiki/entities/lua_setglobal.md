---
title: lua_setglobal
category: entities
created: 2026-04-14T13:46:50.220878+00:00
status: published
---

# lua_setglobal

**Type**: Function  
**Module**: [[lua]]  

## Signature
```lua
void lua_setglobal (lua_State *L, const char *name);
```

## Description
Pops a value from the stack and sets it as the new value of global `name`.

## Parameters
_None_

## Returns
_None_

## Implementation Code
```c
void lua_setglobal (lua_State *L, const char *name);
```
