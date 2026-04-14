---
title: lua_upvalueindex
category: entities
created: 2026-04-14T13:51:47.203330+00:00
status: published
---

# lua_upvalueindex

**Type**: Function  
**Module**: [[lua]]  

## Signature
```lua
int lua_upvalueindex (int i)
```

## Description
Returns the pseudo-index that represents the i-th upvalue of the running function (see §4.2). i must be in the range [1,256].

## Parameters
_None_

## Returns
- (int): The pseudo-index representing the i-th upvalue.

## Implementation Code
```c
int lua_upvalueindex (int i)
```
