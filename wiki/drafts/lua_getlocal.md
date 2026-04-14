---
title: lua_getlocal
category: entities
created: 2026-04-14T10:53:21.866308+00:00
status: draft
---

# lua_getlocal

**Type**: Function  
**Module**: [[lua]]  

## Signature
```lua
const char *lua_getlocal (lua_State *L, const lua_Debug *ar, int n)
```

## Description
Gets information about a local variable or a temporary value of a given activation record or a given function.

## Parameters
- `L` (lua_State*): The Lua state to operate on.
- `ar` (const lua_Debug*): The activation record or the function to inspect.
- `n` (int): The index of the local variable to inspect.

## Returns
- (const char*): The name of the local variable.

## Implementation Code
```c
const char *lua_getlocal (lua_State *L, const lua_Debug *ar, int n);
```
