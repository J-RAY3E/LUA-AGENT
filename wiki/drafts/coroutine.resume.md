---
title: coroutine.resume
category: entities
created: 2026-04-14T20:06:56.951631+00:00
status: draft
---

# coroutine.resume

**Type**: Function  
**Module**: [[Standard Libraries]]  

## Signature
```lua
coroutine.resume(co [, val1, ···])
```

## Description
Starts or continues the execution of coroutine `co`. The first time you resume a coroutine, it starts running its body. The values `val1`, ... are passed as the arguments to the body function. If the coroutine has yielded, `resume` restarts it; the values `val1`, ... are passed as the results from the yield.

## Parameters
_None_

## Returns
- (boolean): true if the coroutine runs without any errors, false if there is any error
- (any): any values passed to `yield` (when the coroutine yields) or any values returned by the body function (when the coroutine terminates)

## Implementation Code
```c
coroutine.resume(co [, val1, ···])
```
