---
title: coroutine.running
category: entities
created: 2026-04-14T20:07:04.786020+00:00
status: draft
---

# coroutine.running

**Type**: Function  
**Module**: [[coroutine]]  

## Signature
```lua
coroutine.running()
```

## Description
Returns the running coroutine plus a boolean, true when the running coroutine is the main one.

## Parameters
_None_

## Returns
- (coroutine): The running coroutine.
- (boolean): True if the running coroutine is the main one.

## Implementation Code
```c
coroutine.running()
```
