---
title: rawlen
category: entities
created: 2026-04-14T21:23:18.356107+00:00
status: published
---

# rawlen

**Type**: Function  
**Module**: [[stdlib]]  

## Signature
```lua
int rawlen(lua_State *L)
```

## Description
Returns the length of the table.

## Parameters
_None_

## Returns
- (int): The length of the table.

## Implementation Code
```c
int rawlen(lua_State *L) { return lua_rawlen(L, 1); }
```
