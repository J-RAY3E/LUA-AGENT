---
title: lua_setmetatable
category: entities
created: 2026-04-14T13:47:42.003236+00:00
status: published
---

# lua_setmetatable

**Type**: Function  
**Module**: [[lua]]  

## Signature
```lua
int lua_setmetatable(lua_State *L, int index)
```

## Description
Pops a table or nil from the stack and sets that value as the new metatable for the value at the given index. (nil means no metatable.) (For historical reasons, this function returns an int, which now is always 1).

## Parameters
_None_

## Returns
- (int): Always 1

## Implementation Code
```c
int lua_setmetatable(lua_State *L, int index);
```
