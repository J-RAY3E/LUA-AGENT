---
title: coroutine.close
category: entities
created: 2026-04-14T20:06:27.007455+00:00
status: draft
---

# coroutine.close

**Type**: Function  
**Module**: [[Standard Libraries]]  

## Signature
```lua
coroutine.close([co])
```

## Description
Closes coroutine `co`, that is, closes all its pending to-be-closed variables and puts the coroutine in a dead state. The default for `co` is the running coroutine.

## Parameters
_None_

## Returns
- (bool): true if the coroutine is closed successfully, false if an error occurs

## Implementation Code
```c
coroutine.close([co])
```
