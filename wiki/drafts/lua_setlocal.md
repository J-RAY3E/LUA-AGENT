---
title: lua_setlocal
category: entities
created: 2026-04-14T13:47:32.348859+00:00
status: draft
---

# lua_setlocal

**Type**: Function  
**Module**: [[lua]]  

## Signature
```lua
lua_setlocal (lua_State *L, const lua_Debug *ar, int n)
```

## Description
Sets the value of a local variable of a given activation record. It assigns the value on the top of the stack to the variable and returns its name. It also pops the value from the stack.

## Parameters
- `L` (lua_State *): The Lua state to operate on.
- `ar` (const lua_Debug *): The activation record to set the local variable in.
- `n` (int): The index of the local variable to set.

## Returns
- (const char *): The name of the local variable.

## Implementation Code
```c
const char *lua_setlocal (lua_State *L, const lua_Debug *ar, int n);
```
