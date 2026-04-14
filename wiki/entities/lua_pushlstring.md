---
title: lua_pushlstring
category: entities
created: 2026-04-14T13:43:06.854170+00:00
status: published
---

# lua_pushlstring

**Type**: Function  
**Module**: [[lua]]  

## Signature
```lua
lua_pushlstring (lua_State *L, const char *s, size_t len)
```

## Description
Pushes the string pointed to by `s` with size `len` onto the stack. Lua will make or reuse an internal copy of the given string, so the memory at `s` can be freed or reused immediately after the function returns. The string can contain any binary data, including embedded zeros.

## Parameters
_None_

## Returns
- (const char *): A pointer to the internal copy of the string (see §4.1.3).

## Implementation Code
```c
const char *lua_pushlstring (lua_State *L, const char *s, size_t len);
```
