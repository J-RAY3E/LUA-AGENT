---
title: lua_pushliteral
category: entities
created: 2026-04-14T13:42:57.128760+00:00
status: draft
---

# lua_pushliteral

**Type**: Function  
**Module**: [[lua]]  

## Signature
```lua
lua_pushliteral (lua_State *L, const char *s)
```

## Description
This macro is equivalent to `lua_pushstring`, but should be used only when `s` is a literal string. (Lua may optimize this case.)

## Parameters
_None_

## Returns
- (const char *): A pointer to the Lua string.

## Implementation Code
```c
const char *lua_pushliteral (lua_State *L, const char *s);
```
