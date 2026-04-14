---
title: luaL_len
category: entities
created: 2026-04-14T16:47:41.816726+00:00
status: draft
---

# luaL_len

**Type**: Function  
**Module**: [[auxiliary library]]  

## Signature
```lua
lua_Integer luaL_len (lua_State *L, int index)
```

## Description
Returns the length of the value at the given index as a number; equivalent to the '#' operator in Lua.

## Parameters
_None_

## Returns
- (lua_Integer): The length of the value at the given index as a number.

## Implementation Code
```c
lua_Integer luaL_len (lua_State *L, int index)
```
