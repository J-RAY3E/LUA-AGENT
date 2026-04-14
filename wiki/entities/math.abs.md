---
title: math.abs
category: entities
created: 2026-04-14T21:14:45.945343+00:00
status: published
---

# math.abs

**Type**: Function  
**Module**: [[Standard Libraries]]  

## Signature
```lua
math.abs(x)
```

## Description
Returns the maximum value between `x` and `-x`. (integer/float)

## Parameters
_None_

## Returns
- (number): The maximum value between `x` and `-x`.

## Implementation Code
```c
return math.max(x, -x)
```
