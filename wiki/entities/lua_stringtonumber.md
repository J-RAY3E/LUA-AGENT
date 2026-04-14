---
title: lua_stringtonumber
category: entities
created: 2026-04-14T13:48:56.950373+00:00
status: published
---

# lua_stringtonumber

**Type**: Function  
**Module**: [[lua]]  

## Signature
```lua
size_t lua_stringtonumber (lua_State *L, const char *s)
```

## Description
Converts the zero-terminated string `s` to a number, pushes that number into the stack, and returns the total size of the string, that is, its length plus one. The conversion can result in an integer or a float, according to the lexical conventions of Lua (see §3.1). The string may have leading and trailing whitespaces and a sign. If the string is not a valid numeral, returns 0 and pushes nothing. (Note that the result can be used as a boolean, true if the conversion succeeds.)

## Parameters
_None_

## Returns
- (size_t): The total size of the string, that is, its length plus one.

## Implementation Code
```c
size_t lua_stringtonumber (lua_State *L, const char *s)
```
