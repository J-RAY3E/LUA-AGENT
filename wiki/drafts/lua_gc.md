---
title: lua_gc
category: entities
created: 2026-04-14T19:43:15.735668+00:00
status: draft
---

# lua_gc

**Type**: Function  
**Module**: [[api_types]]  

## Signature
```lua
lua_gc
```

## Description
Change the garbage collection mode and parameters.

## Parameters
- `mode` (enum): The garbage collection mode.
- `flags` (int): Flags for the garbage collection mode.
- `userdata` (userdata): Userdata to be garbage collected.

## Returns
- (void): No return value.

## Implementation Code
```c
lua_gc
```
