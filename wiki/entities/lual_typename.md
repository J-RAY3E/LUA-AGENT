---
title: luaL_typename
category: entities
created: 2026-04-14T17:11:59.302009+00:00
status: published
---

# luaL_typename

**Type**: Function  
**Module**: [[auxiliary library]]  

## Signature
```lua
const char *luaL_typename (lua_State *L, int index)
```

## Description
Returns the name of the type of the value at the given index.

## Parameters
_None_

## Returns
- (const char *): The name of the type of the value at the given index.

## Implementation Code
```c
const char *luaL_typename (lua_State *L, int index);
```
