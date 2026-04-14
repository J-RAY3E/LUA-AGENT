---
title: lua_rawsetp
category: entities
created: 2026-04-14T13:45:19.376787+00:00
status: draft
---

# lua_rawsetp

**Type**: Function  
**Module**: [[lua]]  

## Signature
```lua
void lua_rawsetp (lua_State *L, int index, const void *p)
```

## Description
Does the equivalent of `t[p] = v`, where `t` is the table at the given index, `p` is encoded as a light userdata, and `v` is the value on the top of the stack. This function pops the value from the stack. The assignment is raw, that is, it does not use the `__newindex` metavalue.

## Parameters
_None_

## Returns
_None_

## Implementation Code
```c
void lua_rawsetp (lua_State *L, int index, const void *p)
```
