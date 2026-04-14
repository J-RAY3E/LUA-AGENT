---
title: string.match
category: entities
created: 2026-04-14T21:26:08.741888+00:00
status: published
---

# string.match

**Type**: Function  
**Module**: [[Standard Libraries]]  

## Signature
```lua
string match(string s, string pattern, integer init)
```

## Description
Looks for the first match of the pattern in the string s. If it finds one, then match returns the captures from the pattern; otherwise it returns 'fail'. If pattern specifies no captures, then the whole match is returned. A third, optional numeric argument init specifies where to start the search; its default value is 1 and can be negative.

## Parameters
- `s` (string): The string to search within.
- `pattern` (string): The pattern to search for.
- `init` (integer): The starting index for the search. Defaults to 1.

## Returns
- (string): The first match of the pattern, or 'fail' if no match is found. If no captures are specified in the pattern, the whole match is returned.

## Implementation Code
```c
string match(string s, string pattern, integer init)
```
