---
title: lua_close
category: entities
created: 2026-04-14T19:07:48.486200+00:00
status: draft
---

# lua_close

**Type**: Function  
**Module**: [[lua]]  

## Signature
```lua
void
```

## Description
Close a value by calling its __close metamethod.

## Parameters
_None_

## Returns
_None_

## Implementation Code
```c
void lua_close(lua_State *L, lua_CFunction metamethod)
```
