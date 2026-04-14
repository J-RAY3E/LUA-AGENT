---
title: debug.setlocal
category: entities
created: 2026-04-14T20:09:18.503750+00:00
status: draft
---

# debug.setlocal

**Type**: Function  
**Module**: [[Standard Libraries]]  

## Signature
```lua
debug.setlocal([thread,] level, local, value)
```

## Description
This function assigns the value `value` to the local variable with index `local` of the function at level `level` of the stack. The function returns **fail** if there is no local variable with the given index, and raises an error when called with a `level` out of range. (You can call `getinfo` to check whether the level is valid.) Otherwise, it returns the name of the local variable.

## Parameters
- `thread` (optional): The thread to set the local variable for.
- `level` (optional): The level of the function on the stack to set the local variable for.
- `local` (optional): The index of the local variable to set the value for.
- `value` (optional): The value to assign to the local variable.

## Returns
- (optional): The name of the local variable if the assignment is successful, otherwise **fail**.

## Implementation Code
```c
nil
```
