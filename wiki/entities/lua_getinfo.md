---
title: lua_getinfo
category: entities
created: 2026-04-14T13:35:05.076960+00:00
status: published
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
- `what` (const char*): The string to specify what information to get. Can be one of the following characters: 'f' for the function being run, 'l' for the current line, 'n' for the function name and what it was called with, 'r' for the function arguments, 'S' for the source file, 't' for the table of arguments, 'u' for the number of arguments, 'L' for the table of lines.
- `ar` (lua_Debug*): A valid activation record that was filled by a previous call to `lua_getstack` or given as argument to a hook (see `lua_Hook`).

## Returns
- (int): Returns 0 to signal an invalid option in `what`; even then the valid options are handled correctly.

## Implementation Code
```c
int lua_getinfo(lua_State *L, const char *what, lua_Debug *ar)
```
