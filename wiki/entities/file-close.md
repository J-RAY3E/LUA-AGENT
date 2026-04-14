---
title: file:close
category: entities
created: 2026-04-14T20:10:50.181814+00:00
status: published
---

# file:close

**Type**: Function  
**Module**: [[file]]  

## Signature
```lua
void file:close()
```

## Description
Closes a file. Note that files are automatically closed when their handles are garbage collected, but that takes an unpredictable amount of time to happen.

## Parameters
_None_

## Returns
_None_

## Implementation Code
```c
void file:close()
```
