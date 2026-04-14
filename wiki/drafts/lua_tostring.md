---
title: lua_tostring
category: entities
created: 2026-04-14T13:50:38.303186+00:00
status: draft
---

# lua_tostring

**Type**: Function  
**Module**: [[lua]]  

## Signature
```lua
lua_tostring (lua_State *L, int index)
```

## Description
Converts a value at the specified index in the Lua stack to a C string.

## Parameters
_None_

## Returns
- (const char *): A C string representing the value at the specified index.

## Implementation Code
```c
const char *lua_tostring (lua_State *L, int index);
```
