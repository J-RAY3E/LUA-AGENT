---
title: assert
category: entities
created: 2026-04-14T20:06:06.114176+00:00
status: draft
---

# assert

**Type**: Function  
**Module**: [[Standard Libraries]]  

## Signature
```lua
assert(v, message)
```

## Description
Raises an error if the value of its argument `v` is false (i.e., nil or false); otherwise, returns all its arguments. In case of error, `message` is the error object; when absent, it defaults to `assertion failed!`

## Parameters
- `v` (any): The value to check for falsiness.
- `message` (string): The error message to display if the value is false.

## Returns
- (any): All arguments passed to the function.

## Implementation Code
```c
assert(v, message)
```
