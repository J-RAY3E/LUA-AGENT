---
title: io.popen
category: entities
created: 2026-04-14T21:13:10.909890+00:00
status: draft
---

# io.popen

**Type**: Function  
**Module**: [[Standard Libraries]]  

## Signature
```lua
prog [, mode]
```

## Description
This function is system dependent and is not available on all platforms. Starts the program `prog` in a separated process and returns a file handle that you can use to read data from this program (if `mode` is "r", the default) or to write data to this program (if `mode` is "w").

## Parameters
- `prog` (const char *): The program to be executed.
- `mode` (const char *): The mode to use for the file handle. Defaults to "r" for reading and "w" for writing.

## Returns
- (FILE *): A file handle that can be used to read or write data to the program.

## Implementation Code
```c
void
```
