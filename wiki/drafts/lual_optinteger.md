---
title: luaL_optinteger
category: entities
created: 2026-04-14T16:49:49.705930+00:00
status: draft
---

# luaL_optinteger

**Type**: Function  
**Module**: [[Auxiliary Library]]  

## Signature
```lua
lua_Integer luaL_optinteger (lua_State *L, int arg, lua_Integer d)
```

## Description
Returns the integer value of the argument `arg` if it is an integer or convertible to an integer. Returns `d` if `arg` is absent or `nil`. Otherwise, raises an error.

## Parameters
- `arg` (int): The argument to be checked for an integer value.
- `d` (lua_Integer): The default value to return if `arg` is absent or `nil`.

## Returns
- (lua_Integer): The integer value of `arg` if it is an integer or convertible to an integer, otherwise `d`.

## Implementation Code
```c
lua_Integer luaL_optinteger (lua_State *L, int arg, lua_Integer d)
```
