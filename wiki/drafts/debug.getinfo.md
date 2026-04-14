---
title: debug.getinfo
category: entities
created: 2026-04-14T20:08:05.720377+00:00
status: draft
---

# debug.getinfo

**Type**: Function  
**Module**: [[Standard Libraries]]  

## Signature
```lua
debug.getinfo([thread,] f [, what])
```

## Description
Returns a table with information about a function. You can give the function directly or you can give a number as the value of f, which means the function running at level f of the call stack of the given thread: level 0 is the current function (getinfo itself); level 1 is the function that called getinfo (except for tail calls, which do not count in the stack); and so on. If f is a number greater than the number of active functions, then getinfo returns fail.

## Parameters
- `thread` (optional): The thread to get information from.
- `f` (optional): The function to get information about.
- `what` (optional): The fields to fill in the returned table.

## Returns
- (table): A table with information about a function.

## Implementation Code
```c
debug.getinfo([thread,] f [, what])
```
