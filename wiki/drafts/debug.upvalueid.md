---
title: debug.upvalueid
category: entities
created: 2026-04-14T20:10:11.536732+00:00
status: draft
---

# debug.upvalueid

**Type**: Function  
**Module**: [[Standard Libraries]]  

## Signature
```lua
f, n -> upvalueid
```

## Description
Returns a unique identifier (as a light userdata) for the upvalue numbered `n` from the given function.

## Parameters
- `f` (function): The function from which to retrieve the upvalue.
- `n` (integer): The index of the upvalue to retrieve.

## Returns
- (userdata): A unique identifier for the upvalue.

## Implementation Code
```c
lua_Alloc, lua_State, lua_Number, etc.
```
