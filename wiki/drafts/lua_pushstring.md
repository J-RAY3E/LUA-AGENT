---
title: lua_pushstring
category: entities
created: 2026-04-14T13:43:33.529948+00:00
status: draft
---

# lua_pushstring

**Type**: Function  
**Module**: [[lua]]  

## Signature
```lua
lua_State *L, const char *s
```

## Description
Pushes the zero-terminated string pointed to by s onto the stack. Lua will make or reuse an internal copy of the given string, so the memory at s can be freed or reused immediately after the function returns.

## Parameters
- `L` (lua_State *): lua_State*
- `s` (const char *): const char *s

## Returns
- (const char *): const char *s

## Implementation Code
```c
const char *lua_pushstring (lua_State *L, const char *s);
```
