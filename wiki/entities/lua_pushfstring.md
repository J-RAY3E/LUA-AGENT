---
title: lua_pushfstring
category: entities
created: 2026-04-14T13:42:24.288531+00:00
status: published
---

# lua_pushfstring

**Type**: Function  
**Module**: [[lua]]  

## Signature
```lua
lua_pushfstring (lua_State *L, const char *fmt, ...)
```

## Description
Pushes onto the stack a formatted string and returns a pointer to this string.

## Parameters
_None_

## Returns
- (const char *): A pointer to the formatted string.

## Implementation Code
```c
const char *lua_pushfstring (lua_State *L, const char *fmt, ...);
```
