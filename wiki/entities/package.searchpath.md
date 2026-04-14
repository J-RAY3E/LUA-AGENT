---
title: package.searchpath
category: entities
created: 2026-04-14T21:22:02.728955+00:00
status: published
---

# package.searchpath

**Type**: Function  
**Module**: [[Standard Libraries]]  

## Signature
```lua
package.searchpath(name, path, sep, rep)
```

## Description
Searches for the given `name` in the given `path`.

## Parameters
- `name` (string): The name to search for.
- `path` (string): The path to search in.
- `sep` (string): The separator character in the path. Defaults to '.'.
- `rep` (string): The replacement character for the separator in the path. Defaults to '/'.

## Returns
- (string): The resulting name of the first file that can be opened in read mode.
- (string): An error message if none of the files can be opened.

## Implementation Code
```c
package.searchpath(name, path, sep, rep)
```
