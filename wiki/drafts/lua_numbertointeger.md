---
title: lua_numbertointeger
category: entities
created: 2026-04-14T13:41:00.246802+00:00
status: draft
---

# lua_numbertointeger

**Type**: Function  
**Module**: [[lua]]  

## Signature
```lua
int lua_numbertointeger (lua_Number n, lua_Integer *p)
```

## Description
Tries to convert a Lua float to a Lua integer; the float `n` must have an integral value. If that value is within the range of Lua integers, it is converted to an integer and assigned to `*p`. The macro results in a boolean indicating whether the conversion was successful. (Note that this range test can be tricky to do correctly without this macro, due to rounding.) This macro may evaluate its arguments more than once.

## Parameters
- `n` (lua_Number): The Lua float to convert.
- `p` (lua_Integer): Pointer to store the converted integer.

## Returns
- (int): 1 if the conversion was successful, 0 otherwise.

## Implementation Code
```c
int lua_numbertointeger (lua_Number n, lua_Integer *p)
```
