---
title: luaL_tolstring
category: entities
created: 2026-04-14T17:11:32.171733+00:00
status: published
---

# luaL_tolstring

**Type**: Function  
**Module**: [[auxiliary library]]  

## Signature
```lua
const char *luaL_tolstring (lua_State *L, int idx, size_t *len)
```

## Description
Converts any Lua value at the given index to a C string in a reasonable format. The resulting string is pushed onto the stack and also returned by the function (see §4.1.3). If `len` is not `NULL`, the function also sets `*len` with the string length.

## Parameters
- `L` (lua_State*): The Lua state to operate on.
- `idx` (int): The index of the Lua value to convert.
- `len` (size_t*): A pointer to store the length of the resulting string.

## Returns
- (const char*): The converted C string.

## Implementation Code
```c
const char *luaL_tolstring (lua_State *L, int idx, size_t *len)
```
