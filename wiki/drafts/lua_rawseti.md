---
title: lua_rawseti
category: entities
created: 2026-04-14T13:45:10.335792+00:00
status: draft
---

# lua_rawseti

**Type**: Function  
**Module**: [[lua]]  

## Signature
```lua
void lua_rawseti (lua_State *L, int index, lua_Integer i);
```

## Description
Does the equivalent of `t[i] = v`, where `t` is the table at the given index and `v` is the value on the top of the stack. This function pops the value from the stack. The assignment is raw, that is, it does not use the `__newindex` metavalue.

## Parameters
_None_

## Returns
_None_

## Implementation Code
```c
void lua_rawseti (lua_State *L, int index, lua_Integer i);
```
