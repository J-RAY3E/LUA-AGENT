---
title: debug.getupvalue
category: entities
created: 2026-04-14T20:08:40.565914+00:00
status: published
---

# debug.getupvalue

**Type**: Function  
**Module**: [[Standard Libraries]]  

## Signature
```lua
f, up -> name, value
```

## Description
Returns the name and value of the upvalue with index `up` of the function `f`. Returns `fail` if there is no upvalue with the given index.

## Parameters
- `f` (function): The function to get the upvalue from.
- `up` (integer): The index of the upvalue to get.

## Returns
- (string): The name of the upvalue.
- (any): The value of the upvalue.

## Implementation Code
```c
lua_getupvalue
```
