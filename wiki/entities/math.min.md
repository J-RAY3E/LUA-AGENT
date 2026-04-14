---
title: math.min
category: entities
created: 2026-04-14T21:16:59.636661+00:00
status: published
---

# math.min

**Type**: Function  
**Module**: [[Standard Libraries]]  

## Signature
```lua
math.min(x, ...) -> number
```

## Description
Returns the argument with the minimum value, according to the Lua operator '<'.

## Parameters
_None_

## Returns
- (number): The minimum value among the arguments.

## Implementation Code
```c
return x < ... ? x : ...
```
