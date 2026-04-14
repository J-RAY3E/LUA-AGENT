---
title: lua_len
category: entities
created: 2026-04-14T13:39:25.209294+00:00
status: published
---

# lua_len

**Type**: Function  
**Module**: [[lua]]  

## Signature
```lua
void lua_len (lua_State *L, int index)
```

## Description
Returns the length of the value at the given index. It is equivalent to the '#' operator in Lua and may trigger a metamethod for the 'length' event.

## Parameters
_None_

## Returns
- (void): None

## Implementation Code
```c
void lua_len (lua_State *L, int index)
```
