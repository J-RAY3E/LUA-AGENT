---
title: lua_rawget
category: entities
created: 2026-04-14T13:44:22.071501+00:00
status: draft
---

# lua_rawget

**Type**: Function  
**Module**: [[lua]]  

## Signature
```lua
int lua_rawget(lua_State *L, int index)
```

## Description
Similar to `lua_gettable`, but does a raw access (i.e., without metamethods). The value at `index` must be a table.

## Parameters
_None_

## Returns
- (int): Returns the value at the specified index in the Lua state.

## Implementation Code
```c
int lua_rawget(lua_State *L, int index)
```
