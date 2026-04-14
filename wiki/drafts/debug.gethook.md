---
title: debug.gethook
category: entities
created: 2026-04-14T20:07:53.538830+00:00
status: draft
---

# debug.gethook

**Type**: Function  
**Module**: [[Standard Libraries]]  

## Signature
```lua
debug.gethook([thread])
```

## Description
Returns the current hook settings of the thread, as three values: the current hook function, the current hook mask, and the current hook count, as set by the `debug.sethook` function.

## Parameters
_None_

## Returns
- (table): The current hook function, the current hook mask, and the current hook count.

## Implementation Code
```c
nil
```
