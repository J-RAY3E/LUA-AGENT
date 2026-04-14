---
title: pairs
category: entities
created: 2026-04-14T21:22:15.836861+00:00
status: draft
---

# pairs

**Type**: Function  
**Module**: [[Standard Libraries]]  

## Signature
```lua
pairs(t)
```

## Description
If `t` has a metamethod `__pairs`, calls it with `t` as argument and returns the first four results from the call. Otherwise, returns the `next` function, the table `t`, plus two `nil` values, so that the construction `for k,v in pairs(t) do body end` will iterate over all key–value pairs of table `t`. See function `next` for the caveats of modifying the table during its traversal.

## Parameters
_None_

## Returns
- (function): If `t` has a metamethod `__pairs`, calls it with `t` as argument and returns the first four results from the call. Otherwise, returns the `next` function, the table `t`, plus two `nil` values, so that the construction `for k,v in pairs(t) do body end` will iterate over all key–value pairs of table `t`. See function `next` for the caveats of modifying the table during its traversal.

## Implementation Code
```c

```
