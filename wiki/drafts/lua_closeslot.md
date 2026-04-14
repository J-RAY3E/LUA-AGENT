---
title: lua_closeslot
category: entities
created: 2026-04-14T13:31:50.558733+00:00
status: draft
---

# lua_closeslot

**Type**: Function  
**Module**: [[lua]]  

## Signature
```lua
void lua_closeslot (lua_State *L, int index)
```

## Description
Close the to-be-closed slot at the given index and set its value to nil. The index must be the last index previously marked to be closed (see `lua_toclose`) that is still active (that is, not closed yet). A `__close` metamethod cannot yield when called through this function.

## Parameters
_None_

## Returns
_None_

## Implementation Code
```c
void lua_closeslot (lua_State *L, int index)
```
