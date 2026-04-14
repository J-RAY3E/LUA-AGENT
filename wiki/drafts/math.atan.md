---
title: math.atan
category: entities
created: 2026-04-14T21:15:13.081166+00:00
status: draft
---

# math.atan

**Type**: Function  
**Module**: [[math]]  

## Signature
```lua
math.atan(y [, x])
```

## Description
Returns the arc tangent of y/x (in radians), using the signs of both arguments to find the quadrant of the result. It also handles correctly the case of x being zero.

## Parameters
- `y` (number): The value to compute the arc tangent of.
- `x` (number): The value to compute the arc tangent of. Defaults to 1.

## Returns
- (number): The arc tangent of y/x (in radians).

## Implementation Code
```c
math.atan(y [, x])
```
