---
title: lua_setfield
category: entities
created: 2026-04-14T13:46:41.836183+00:00
status: published
---

# lua_setfield

**Type**: Function  
**Module**: [[lua]]  

## Signature
```lua
void lua_setfield(lua_State *L, int index, const char *k)
```

## Description
Does the equivalent to `t[k] = v`, where `t` is the value at the given index and `v` is the value on the top of the stack.

## Parameters
- `L` (lua_State*): The Lua state to operate on.
- `index` (int): The index of the table or value to set the field on.
- `k` (const char*): The key to set the field on.

## Returns
- (void): None

## Implementation Code
```c
void lua_setfield (lua_State *L, int index, const char *k);
```
