---
title: require
category: entities
created: 2026-04-14T21:23:36.525336+00:00
status: draft
---

# require

**Type**: Function  
**Module**: [[Standard Libraries]]  

## Signature
```lua
require (modname)
```

## Description
Loads the given module. The function starts by looking into the `package.loaded` table to determine whether `modname` is already loaded. If it is, then `require` returns the value stored at `package.loaded[modname]`. Otherwise, it tries to find a loader for the module.

## Parameters
_None_

## Returns
- (any): The value stored at `package.loaded[modname]` if `modname` is already loaded, otherwise the loader data returned by the searcher.

## Implementation Code
```c
require(modname)
```
