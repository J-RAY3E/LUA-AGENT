---
title: lua_getupvalue
category: entities
created: 2026-04-14T13:36:20.457247+00:00
status: published
---

# lua_getupvalue

**Type**: Function  
**Module**: [[lua]]  

## Signature
```lua
lua_getupvalue (lua_State *L, int funcindex, int n)
```

## Description
Gets information about the n-th upvalue of the closure at index funcindex. It pushes the upvalue's value onto the stack and returns its name. Returns NULL (and pushes nothing) when the index n is greater than the number of upvalues.

## Parameters
- `L` (lua_State*): The Lua state to operate on.
- `funcindex` (int): The index of the closure.
- `n` (int): The index of the upvalue.

## Returns
- (const char*): The name of the upvalue.

## Implementation Code
```c
const char *lua_getupvalue (lua_State *L, int funcindex, int n);
```
