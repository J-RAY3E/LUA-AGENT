---
title: lua_pushexternalstring
category: entities
created: 2026-04-14T13:42:15.343521+00:00
status: draft
---

# lua_pushexternalstring

**Type**: Function  
**Module**: [[lua]]  

## Signature
```lua
lua_pushexternalstring (lua_State *L, const char *s, size_t len, lua_Alloc falloc, void *ud)
```

## Description
Creates an external string, a string that uses memory not managed by Lua.

## Parameters
- `L` (lua_State*): The Lua state to operate on.
- `s` (const char*): Pointer to the external buffer holding the string content.
- `len` (size_t): Length of the string.
- `falloc` (lua_Alloc): Function to allocate memory for the external buffer.
- `ud` (void*): User data for the function.

## Returns
- (const char*): Pointer to the string.

## Implementation Code
```c
const char *lua_pushexternalstring (lua_State *L, const char *s, size_t len, lua_Alloc falloc, void *ud);
```
