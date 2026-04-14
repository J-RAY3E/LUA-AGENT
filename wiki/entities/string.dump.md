---
title: string.dump
category: entities
created: 2026-04-14T21:24:49.349320+00:00
status: published
---

# string.dump

**Type**: Function  
**Module**: [[Standard Libraries]]  

## Signature
```lua
function (function [, strip])
```

## Description
Returns a string containing a binary representation (a *binary chunk*) of the given function, so that a later `load` on this string returns a copy of the function (but with new upvalues). If `strip` is a true value, the binary representation may not include all debug information about the function, to save space.

## Parameters
- `function` (function): The function to be dumped.
- `strip` (boolean): If true, the binary representation may not include all debug information about the function, to save space.

## Returns
- (string): A string containing a binary representation (a *binary chunk*) of the given function.

## Implementation Code
```c
string.dump
```
