---
title: math.frexp
category: entities
created: 2026-04-14T21:16:11.494125+00:00
status: published
---

# math.frexp

**Type**: Function  
**Module**: [[math]]  

## Signature
```lua
math.frexp(x)
```

## Description
Returns two numbers m and e such that x = m * 2^e, where e is an integer. When x is zero, NaN, +inf, or -inf, m is equal to x; otherwise, the absolute value of m is in the range [0.5, 1).

## Parameters
_None_

## Returns
- (number): m
- (number): e

## Implementation Code
```c
math.frexp(x)
```
