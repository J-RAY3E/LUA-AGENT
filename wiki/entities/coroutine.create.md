---
title: coroutine.create
category: entities
created: 2026-04-14T20:06:34.831828+00:00
status: published
---

# coroutine.create

**Type**: Function  
**Module**: [[Standard Libraries]]  

## Signature
```lua
coroutine.create(f)
```

## Description
Creates a new coroutine, with body `f`. `f` must be a function. Returns this new coroutine, an object with type "thread".

## Parameters
_None_

## Returns
- (thread): The new coroutine object.

## Implementation Code
```c
coroutine.create(f)
```
