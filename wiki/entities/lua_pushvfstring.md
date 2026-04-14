---
title: lua_pushvfstring
category: entities
created: 2026-04-14T13:44:01.506755+00:00
status: published
---

# lua_pushvfstring

**Type**: Function  
**Module**: [[lua]]  

## Signature
```lua
lua_pushvfstring (lua_State *L, const char *fmt, va_list argp)
```

## Description
Push a formatted string onto the stack, similar to `lua_pushfstring` but with a `va_list` instead of a variable number of arguments. It does not raise errors and instead pushes the error message and returns `NULL` in case of errors.

## Parameters
_None_

## Returns
- (const char *): The formatted string pushed onto the stack.

## Implementation Code
```c
const char *lua_pushvfstring (lua_State *L, const char *fmt, va_list argp);
```
