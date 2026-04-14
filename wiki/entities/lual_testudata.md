---
title: luaL_testudata
category: entities
created: 2026-04-14T17:11:18.467018+00:00
status: published
---

# luaL_testudata

**Type**: Function  
**Module**: [[auxiliary library]]  

## Signature
```lua
void *luaL_testudata (lua_State *L, int arg, const char *tname)
```

## Description
Works like `luaL_checkudata`, except that, when the test fails, it returns `NULL` instead of raising an error.

## Parameters
_None_

## Returns
- (void *): Returns a pointer to the userdata if the test passes, or `NULL` if the test fails.

## Implementation Code
```c
void *luaL_testudata (lua_State *L, int arg, const char *tname)
```
