---
title: os.tmpname
category: entities
created: 2026-04-14T21:20:45.129372+00:00
status: published
---

# os.tmpname

**Type**: Function  
**Module**: [[stdlib]]  

## Signature
```lua
string os.tmpname()
```

## Description
Returns a string with a file name that can be used for a temporary file. The file must be explicitly opened before its use and explicitly removed when no longer needed.

## Parameters
_None_

## Returns
- (string): A string with a file name that can be used for a temporary file.

## Implementation Code
```c
os.tmpname
```
