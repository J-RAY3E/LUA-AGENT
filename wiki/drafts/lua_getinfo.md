---
title: lua_getinfo
category: entities
created: 2026-04-14T10:52:56.515623+00:00
status: draft
---

# lua_getinfo

**Type**: Function  
**Module**: [[lua]]  

## Signature
```lua
int lua_getinfo(lua_State *L, const char *what, lua_Debug *ar)
```

## Description
Gets information about a specific function or function invocation.

## Parameters
- `L` (lua_State*): The Lua state to operate on.
- `what` (const char*): The string specifying what information to get. Can be one of 'f', 'l', 'n', 'r', 'S', 't', 'u', 'L'.
- `ar` (lua_Debug*): A valid activation record that was filled by a previous call to `lua_getstack` or given as argument to a hook.

## Returns
- (int): 0 to signal an invalid option in `what`; even then the valid options are handled correctly.

## Implementation Code
```c
int lua_getinfo(lua_State *L, const char *what, lua_Debug *ar)
```
