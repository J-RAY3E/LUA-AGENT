---
title: coroutine.isyieldable
category: entities
created: 2026-04-14T20:06:46.013000+00:00
status: draft
---

# coroutine.isyieldable

**Type**: Function  
**Module**: [[coroutine]]  

## Signature
```lua
coroutine.isyieldable(co)
```

## Description
Returns true when the coroutine `co` can yield. The default for `co` is the running coroutine.

## Parameters
- `co` (coroutine): The coroutine to check for yieldability.

## Returns
- (boolean): true if the coroutine can yield, false otherwise.

## Implementation Code
```c
coroutine.isyieldable(co)
```
