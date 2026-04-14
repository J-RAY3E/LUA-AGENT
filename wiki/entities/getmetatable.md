---
title: getmetatable
category: entities
created: 2026-04-14T20:12:16.537939+00:00
status: published
---

# getmetatable

**Type**: Function  
**Module**: [[Standard Libraries]]  

## Signature
```lua
getmetatable(object)
```

## Description
If `object` does not have a metatable, returns **nil**. Otherwise, if the object's metatable has a `__metatable` field, returns the associated value. Otherwise, returns the metatable of the given object.

## Parameters
_None_

## Returns
- (nil): If `object` does not have a metatable, returns **nil**. Otherwise, if the object's metatable has a `__metatable` field, returns the associated value. Otherwise, returns the metatable of the given object.

## Implementation Code
```c
getmetatable(object)
```
