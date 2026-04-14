---
title: string.format
category: entities
created: 2026-04-14T21:25:19.586454+00:00
status: published
---

# string.format

**Type**: Function  
**Module**: [[Standard Libraries]]  

## Signature
```lua
string format(string formatstring, ...) -> string
```

## Description
Returns a formatted version of its variable number of arguments following the description given in its first argument, which must be a string. The format string follows the same rules as the ISO C function `sprintf`. The accepted conversion specifiers are `A`, `a`, `c`, `d`, `E`, `e`, `f`, `G`, `g`, `i`, `o`, `p`, `s`, `u`, `X`, `x`, and '`%`', plus a non-C specifier `q'. The accepted flags are '`-`', '`+`', '`#`', '`0`', and '' (space). Both width and precision, when present, are limited to two digits.

## Parameters
_None_

## Returns
- (string): A formatted version of its variable number of arguments following the description given in its first argument, which must be a string. The format string follows the same rules as the ISO C function `sprintf'. The accepted conversion specifiers are `A`, `a`, `c`, `d`, `E`, `e`, `f`, `G`, `g`, `i`, `o`, `p`, `s`, `u`, `X`, `x`, and '`%`', plus a non-C specifier `q'. The accepted flags are '`-`', '`+`', '`#`', '`0`', and '' (space). Both width and precision, when present, are limited to two digits.

## Implementation Code
```c
string.format(formatstring, ...) -> string
```
