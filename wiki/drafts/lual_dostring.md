---
title: luaL_dostring
category: entities
created: 2026-04-14T16:46:20.569228+00:00
status: draft
---

# luaL_dostring

**Type**: Function  
**Module**: [[auxiliary library]]  

## Signature
```lua
int luaL_dostring (lua_State *L, const char *str)
```

## Description
Loads and runs the given string. It is defined as the following macro: luaL_loadstring(L, str) || lua_pcall(L, 0, LUA_MULTRET, 0)

## Parameters
_None_

## Returns
- (int): 0 if there are no errors, 1 in case of errors

## Implementation Code
```c
luaL_loadstring(L, str) || lua_pcall(L, 0, LUA_MULTRET, 0)
```
