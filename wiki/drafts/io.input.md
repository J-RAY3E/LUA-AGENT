---
title: io.input
category: entities
created: 2026-04-14T20:12:43.479388+00:00
status: draft
---

# io.input

**Type**: Function  
**Module**: [[Standard Libraries]]  

## Signature
```lua
file_or_handle
```

## Description
When called with a file name, it opens the named file (in text mode), and sets its handle as the default input file. When called with a file handle, it simply sets this file handle as the default input file. When called without arguments, it returns the current default input file.

## Parameters
- `file_or_handle` (file_or_handle): The file name or file handle to open or set as the default input file.

## Returns
- (file_or_handle): The current default input file.

## Implementation Code
```c
void
```
