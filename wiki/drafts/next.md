---
title: next
category: entities
created: 2026-04-14T21:18:55.331362+00:00
status: draft
---

# next

**Type**: Function  
**Module**: [[Standard Libraries]]  

## Signature
```lua
next(table, index)
```

## Description
Allows a program to traverse all fields of a table. Its first argument is a table and its second argument is an index in this table. A call to `next` returns the next index of the table and its associated value. When called with **nil** as its second argument, `next` returns an initial index and its associated value. When called with the last index, or with **nil** in an empty table, `next` returns **nil**. If the second argument is absent, then it is interpreted as **nil**. In particular, you can use `next(t)` to check whether a table is empty.

## Parameters
- `table` (table): The table to traverse.
- `index` (integer): The index in the table to start the traversal.

## Returns
- (table): The next index and its associated value.

## Implementation Code
```c
next
```
