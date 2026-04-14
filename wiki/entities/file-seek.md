---
title: file:seek
category: entities
created: 2026-04-14T20:11:32.666766+00:00
status: published
---

# file:seek

**Type**: Function  
**Module**: [[Standard Libraries]]  

## Signature
```lua
file:seek([whence [, offset]])
```

## Description
Sets and gets the file position, measured from the beginning of the file, to the position given by `offset` plus a base specified by the string `whence`, as follows:
* `set`: base is position 0 (beginning of the file);
* `cur`: base is current position;
* `end`: base is end of file;

In case of success, `seek` returns the final file position, measured in bytes from the beginning of the file. If `seek` fails, it returns `fail`, plus a string describing the error.

The default value for `whence` is `"cur"`, and for `offset` is 0. Therefore, the call `file:seek()` returns the current file position, without changing it; the call `file:seek("set")` sets the position to the beginning of the file (and returns 0); and the call `file:seek("end")` sets the position to the end of the file, and returns its size.

## Parameters
- `whence` (string): Specifies the base for the position. Can be `"set"`, `"cur"`, or `"end"`.
- `offset` (number): The offset from the base specified by `whence`.

## Returns
- (number): The final file position, measured in bytes from the beginning of the file.
- (string): A string describing the error if `seek` fails.

## Implementation Code
```c
file:seek([whence [, offset]])
```
