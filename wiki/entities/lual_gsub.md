---
title: luaL_gsub
category: entities
created: 2026-04-14T16:47:32.590952+00:00
status: published
---

# luaL_gsub

**Type**: Function  
**Module**: [[Auxiliary Library]]  

## Signature
```lua
const char *luaL_gsub (lua_State *L, const char *s, const char *p, const char *r)
```

## Description
Creates a copy of string `s`, replacing any occurrence of the string `p` with the string `r`. Pushes the resulting string on the stack and returns it.

## Parameters
_None_

## Returns
- (const char *): The resulting string after replacing occurrences of `p` with `r`.

## Implementation Code
```c
const char *luaL_gsub (lua_State *L, const char *s, const char *p, const char *r)
```
