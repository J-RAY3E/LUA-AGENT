---
title: package.loadlib
category: entities
created: 2026-04-14T21:21:20.413254+00:00
status: draft
---

# package.loadlib

**Type**: Function  
**Module**: [[Standard Libraries]]  

## Signature
```lua
package.loadlib (libname, funcname)
```

## Description
Dynamically links the host program with the C library `libname`. If `funcname` is `*`, it only links with the library, making the symbols exported by the library available to other dynamically linked libraries. Otherwise, it looks for a function `funcname` inside the library and returns this function as a C function.

## Parameters
_None_

## Returns
- (void): None

## Implementation Code
```c
package.loadlib (libname, funcname)
```
