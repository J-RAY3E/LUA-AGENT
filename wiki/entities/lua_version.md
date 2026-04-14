---
title: lua_version
category: entities
created: 2026-04-14T13:52:06.953638+00:00
status: published
---

# lua_version

**Type**: Function  
**Module**: [[lua]]  

## Signature
```lua
lua_Number lua_version (lua_State *L)
```

## Description
Returns the version number of this core.

## Parameters
_None_

## Returns
- (lua_Number): The version number of this core.

## Implementation Code
```c
lua_Number lua_version (lua_State *L);
```
