---
title: math.random
category: entities
created: 2026-04-14T21:17:40.535535+00:00
status: draft
---

# math.random

**Type**: Function  
**Module**: [[Standard Libraries]]  

## Signature
```lua
math.random([m, n])
```

## Description
When called without arguments, returns a pseudo-random float with uniform distribution in the range [0, 1). When called with two integers m and n, math.random returns a pseudo-random integer with uniform distribution in the range [m, n]. The call math.random(n), for a positive n, is equivalent to math.random(1, n). The call math.random(0) produces an integer with all bits (pseudo)random.

## Parameters
_None_

## Returns
- (number): A pseudo-random float or integer

## Implementation Code
```c
math.random([m, n])
```
