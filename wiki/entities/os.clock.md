---
title: os.clock
category: entities
created: 2026-04-14T21:19:02.952314+00:00
status: published
---

# os.clock

**Type**: Function  
**Module**: [[Standard Libraries]]  

## Signature
```lua
void os.clock(void)
```

## Description
Returns an approximation of the amount in seconds of CPU time used by the program, as returned by the underlying ISO C function `clock`.

## Parameters
_None_

## Returns
_None_

## Implementation Code
```c
void os_clock(void)
```
