---
title: select
category: entities
created: 2026-04-14T21:23:47.045297+00:00
status: published
---

# select

**Type**: Function  
**Module**: [[Standard Libraries]]  

## Signature
```lua
select(index, ...) -> any
```

## Description
If index is a number, returns all arguments after argument number index; a negative number indexes from the end (-1 is the last argument). Otherwise, index must be the string "#", and select returns the total number of extra arguments it received.

## Parameters
_None_

## Returns
_None_

## Implementation Code
```c
select(index, ...) -> any
```
