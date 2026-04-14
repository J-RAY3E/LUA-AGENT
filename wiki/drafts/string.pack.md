---
title: string.pack
category: entities
created: 2026-04-14T21:26:18.068043+00:00
status: draft
---

# string.pack

**Type**: Function  
**Module**: [[Standard Libraries]]  

## Signature
```lua
string.pack(fmt, v1, v2, ···)
```

## Description
Returns a binary string containing the values `v1`, `v2`, etc. serialized in binary form (packed) according to the format string `fmt` (see §6.5.2).

## Parameters
_None_

## Returns
- (string): A binary string containing the values `v1`, `v2`, etc. serialized in binary form (packed) according to the format string `fmt` (see §6.5.2).

## Implementation Code
```c
string.pack(fmt, v1, v2, ···)
```
