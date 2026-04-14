---
title: pcall
category: entities
created: 2026-04-14T21:22:42.302826+00:00
status: published
---

# pcall

**Type**: Function  
**Module**: [[Standard Libraries]]  

## Signature
```lua
pcall (f [, arg1, ···])
```

## Description
Calls the function `f` with the given arguments in *protected mode*. This means that any error inside `f` is not propagated; instead, `pcall` catches the error and returns a status code. Its first result is the status code (a boolean), which is **true** if the call succeeds without errors. In such case, `pcall` also returns all results from the call, after this first result. In case of any error, `pcall` returns **false** plus the error object. Note that errors caught by `pcall` do not call a message handler.

## Parameters
_None_

## Returns
- (boolean): true if the call succeeds without errors. false if an error occurs.
- (table): All results from the call, after the first result.

## Implementation Code
```c
lua_pcall
```
