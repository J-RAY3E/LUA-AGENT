---
title: file:write
category: entities
created: 2026-04-14T20:11:50.645879+00:00
status: draft
---

# file:write

**Type**: Function  
**Module**: [[Standard Libraries]]  

## Signature
```lua
file:write (···)
```

## Description
Writes the value of each of its arguments to `file`. The arguments must be strings or numbers.

## Parameters
_None_

## Returns
- (file): Returns `file` on success, or four values on failure.

## Implementation Code
```c
lua_Alloc, lua_State, lua_Number, etc.
```
