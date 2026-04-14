---
title: coroutine.status
category: entities
created: 2026-04-14T20:07:15.696211+00:00
status: published
---

# coroutine.status

**Type**: Function  
**Module**: [[Standard Libraries]]  

## Signature
```lua
coroutine.status (co)
```

## Description
Returns the status of the coroutine `co`, as a string: "running", if the coroutine is running (that is, it is the one that called `status`); "suspended", if the coroutine is suspended in a call to `yield`, or if it has not started running yet; "normal", if the coroutine is active but not running (that is, it has resumed another coroutine); and "dead", if the coroutine has finished its body function, or if it has stopped with an error.

## Parameters
_None_

## Returns
- (string): The status of the coroutine `co`, as a string: "running", if the coroutine is running (that is, it is the one that called `status`); "suspended", if the coroutine is suspended in a call to `yield`, or if it has not started running yet; "normal", if the coroutine is active but not running (that is, it has resumed another coroutine); and "dead", if the coroutine has finished its body function, or if it has stopped with an error.

## Implementation Code
```c

```
