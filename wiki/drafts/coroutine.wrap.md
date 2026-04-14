---
title: coroutine.wrap
category: entities
created: 2026-04-14T20:07:27.454711+00:00
status: draft
---

# coroutine.wrap

**Type**: Function  
**Module**: [[Standard Libraries]]  

## Signature
```lua
coroutine.wrap(f)
```

## Description
Creates a new coroutine, with body `f`; `f` must be a function. Returns a function that resumes the coroutine each time it is called. Any arguments passed to this function behave as the extra arguments to `resume`. The function returns the same values returned by `resume`, except the first boolean. In case of error, the function closes the coroutine and propagates the error.

## Parameters
_None_

## Returns
- (function): Returns a function that resumes the coroutine each time it is called. Any arguments passed to this function behave as the extra arguments to `resume`. The function returns the same values returned by `resume`, except the first boolean. In case of error, the function closes the coroutine and propagates the error.

## Implementation Code
```c
coroutine.wrap(f)
```
