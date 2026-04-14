---
title: string.find
category: entities
created: 2026-04-14T21:25:02.078542+00:00
status: draft
---

# string.find

**Type**: Function  
**Module**: [[Standard Libraries]]  

## Signature
```lua
s, pattern [, init [, plain]]
```

## Description
Looks for the first match of `pattern` in the string `s`. If it finds a match, then `find` returns the indices of `s` where this occurrence starts and ends; otherwise, it returns `fail`. A third, optional numeric argument `init` specifies where to start the search; its default value is 1 and can be negative. A **true** as a fourth, optional argument `plain` turns off the pattern matching facilities, so the function does a plain "find substring" operation, with no characters in `pattern` being considered magic.

## Parameters
- `s` (string): The string to search within.
- `pattern` (string): The pattern to search for.
- `init` (number): The starting index for the search. Defaults to 1.
- `plain` (boolean): If true, performs a plain substring search without pattern matching.

## Returns
- (table): A table containing the start and end indices of the match, or `fail` if no match is found.

## Implementation Code
```c
lua_Alloc, lua_State, lua_Number, etc.
```
