---
title: string.unpack
category: entities
created: 2026-04-14T20:12:06.979426+00:00
status: draft
---

# string.unpack

**Type**: Function  
**Module**: [[pdf]]  

## Signature
```lua
string.unpack(format, data)
```

## Description
Unpacks the data from the given format string.

## Parameters
- `format` (string): The format string describing the layout of the structure.
- `data` (string): The data to be unpacked.

## Returns
- (any): The unpacked data.

## Implementation Code
```c
string.unpack(format, data)
```
