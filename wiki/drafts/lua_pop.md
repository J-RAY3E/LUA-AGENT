---
title: lua_pop
category: entities
created: 2026-04-14T13:41:35.405785+00:00
status: draft
---

# lua_pop

**Type**: Function  
**Module**: [[lua]]  

## Signature
```lua
void lua_pop(lua_State *L, int n);
```

## Description
Pops `n` elements from the stack. It is implemented as a macro over `lua_settop`.

## Parameters
_None_

## Returns
_None_

## Implementation Code
```c
void lua_pop(lua_State *L, int n);
```
