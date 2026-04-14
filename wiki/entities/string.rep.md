---
title: string.rep
category: entities
created: 2026-04-14T21:26:37.087331+00:00
status: published
---

# string.rep

**Type**: Function  
**Module**: [[Standard Libraries]]  

## Signature
```lua
string rep(string s, number n, string sep = '')
```

## Description
Returns a string that is the concatenation of n copies of the string s separated by the string sep. The default value for sep is the empty string (that is, no separator). Returns the empty string if n is not positive.

## Parameters
- `s` (string): The string to be repeated.
- `n` (number): The number of times the string s should be repeated.
- `sep` (string): The separator string. Defaults to the empty string.

## Returns
- (string): The resulting string.

## Implementation Code
```c
string rep(string s, number n, string sep = '')
```
