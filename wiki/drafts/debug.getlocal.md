---
title: debug.getlocal
category: entities
created: 2026-04-14T20:08:16.728362+00:00
status: draft
---

# debug.getlocal

**Type**: Function  
**Module**: [[Standard Libraries]]  

## Signature
```lua
debug.getlocal([thread,] f, local)
```

## Description
This function returns the name and the value of the local variable with index `local` of the function at level `f` of the stack. This function accesses not only explicit local variables, but also parameters and temporary values.

## Parameters
- `thread` (optional): The thread to get the local variable from.
- `f` (optional): The function to get the local variable from.
- `local` (integer): The index of the local variable to get.

## Returns
- (string): The name and value of the local variable.

## Implementation Code
```c
lua_Alloc, lua_State, lua_Number, etc.
```
