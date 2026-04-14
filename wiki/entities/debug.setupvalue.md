---
title: debug.setupvalue
category: entities
created: 2026-04-14T20:09:39.143201+00:00
status: published
---

# debug.setupvalue

**Type**: Function  
**Module**: [[Standard Libraries]]  

## Signature
```lua
debug.setupvalue(f, up, value)
```

## Description
This function assigns the value `value` to the upvalue with index `up` of the function `f`. The function returns **fail** if there is no upvalue with the given index. Otherwise, it returns the name of the upvalue.

## Parameters
- `f` (function): The function whose upvalue is being assigned.
- `up` (integer): The index of the upvalue to be assigned.
- `value` (any): The value to be assigned to the upvalue.

## Returns
- (string): The name of the upvalue.

## Implementation Code
```c
lua_Alloc, lua_State, lua_Number, etc.
```
