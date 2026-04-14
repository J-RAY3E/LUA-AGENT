---
title: lua_tointeger
category: entities
created: 2026-04-14T13:49:32.866173+00:00
status: draft
---

# lua_tointeger

**Type**: Function  
**Module**: [[lua]]  

## Signature
```lua
lua_Integer lua_tointeger (lua_State *L, int index)
```

## Description
lua_tointeger - Extracts an integer from a Lua table or environment.

## Parameters
_None_

## Returns
- (lua_Integer): The integer value extracted from the Lua table or environment.

## Implementation Code
```c
lua_Integer lua_tointeger (lua_State *L, int index);
```
