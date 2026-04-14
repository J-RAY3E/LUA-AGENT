---
title: math.randomseed
category: entities
created: 2026-04-14T21:17:51.832808+00:00
status: published
---

# math.randomseed

**Type**: Function  
**Module**: [[Standard Libraries]]  

## Signature
```lua
math.randomseed(x, y)
```

## Description
When called with at least one argument, the integer parameters x and y are joined into a seed that is used to reinitialize the pseudo-random generator; equal seeds produce equal sequences of numbers. The default for y is zero. When called with no arguments, Lua generates a seed with a weak attempt for randomness. This function returns the two seed components that were effectively used, so that setting them again repeats the sequence. To ensure a required level of randomness to the initial state (or contrarily, to have a deterministic sequence, for instance when debugging a program), you should call math.randomseed with explicit arguments.

## Parameters
- `x` (integer): The first seed component.
- `y` (integer): The second seed component.

## Returns
- (integer): The two seed components that were effectively used.

## Implementation Code
```c
math.randomseed(x, y)
```
