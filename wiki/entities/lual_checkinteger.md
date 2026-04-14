---
title: luaL_checkinteger
category: entities
created: 2026-04-14T16:44:05.905084+00:00
status: published
---

# luaL_checkinteger

**Type**: Function  
**Module**: [[Auxiliary Library]]  

## Signature
```lua
lua_Integer luaL_checkinteger (lua_State *L, int arg)
```

## Description
Checks whether the function argument `arg` is an integer (or can be converted to an integer) and returns this integer.

## Parameters
_None_

## Returns
- (lua_Integer): The integer value if `arg` is an integer or can be converted to an integer, otherwise 0.

## Implementation Code
```c
lua_Integer luaL_checkinteger (lua_State *L, int arg)
```
