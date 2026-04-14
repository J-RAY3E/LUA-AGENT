---
title: setmetatable
category: entities
created: 2026-04-14T21:23:59.142505+00:00
status: published
---

# setmetatable

**Type**: Function  
**Module**: [[Standard Libraries]]  

## Signature
```lua
table setmetatable(table, metatable)
```

## Description
Sets the metatable for the given table. If `metatable` is nil, removes the metatable of the given table. If the original metatable has a __metatable field, raises an error.

## Parameters
- `table` (table): The table to set or remove the metatable for.
- `metatable` (table): The metatable to set or remove.

## Returns
- (table): The original table.

## Implementation Code
```c
nil
```
