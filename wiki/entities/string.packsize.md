---
title: string.packsize
category: entities
created: 2026-04-14T21:26:26.264179+00:00
status: published
---

# string.packsize

**Type**: Function  
**Module**: [[Standard Libraries]]  

## Signature
```lua
string.packsize(fmt)
```

## Description
Returns the length of a string resulting from `string.pack` with the given format. The format string cannot have the variable-length options 's' or 'z' (see §6.5.2).

## Parameters
_None_

## Returns
- (integer): The length of the resulting string.

## Implementation Code
```c
string.packsize(fmt)
```
