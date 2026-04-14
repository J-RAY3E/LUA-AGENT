---
title: lua_call
category: entities
created: 2026-04-14T10:38:17.055282+00:00
status: published
---

# lua_call

**Type**: Function  
**Module**: [[lua]]  

## Signature
```lua
int
```

## Description
Executes a Lua function.

## Parameters
- `lua_State*` (lua_State*): The Lua state to execute the function in.
- `int` (int): The index of the function to execute.

## Returns
- (int): The return value of the function.

## Implementation Code
```c
lua_call
```
