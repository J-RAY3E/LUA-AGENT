---
title: debug.setuservalue
category: entities
created: 2026-04-14T20:09:51.072652+00:00
status: published
---

# debug.setuservalue

**Type**: Function  
**Module**: [[Standard Libraries]]  

## Signature
```lua
udata value, n
```

## Description
Sets the given `value` as the `n`-th user value associated to the given `udata`. `udata` must be a full userdata.

## Parameters
- `udata` (userdata): The userdata to associate the value with.
- `value` (value): The value to set as the user value.
- `n` (integer): The index of the user value to set.

## Returns
- (udata): The userdata.
- (error): If the userdata does not have that value, returns 'fail'.

## Implementation Code
```c
void
```
