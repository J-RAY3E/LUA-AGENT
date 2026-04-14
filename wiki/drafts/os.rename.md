---
title: os.rename
category: entities
created: 2026-04-14T21:20:13.423859+00:00
status: draft
---

# os.rename

**Type**: Function  
**Module**: [[Standard Libraries]]  

## Signature
```lua
os.rename (oldname, newname)
```

## Description
Renames the file or directory named `oldname` to `newname`. If this function fails, it returns **fail**, plus a string describing the error and the error code. Otherwise, it returns true.

## Parameters
_None_

## Returns
- (string): A string describing the error and the error code.

## Implementation Code
```c
os.rename
```
