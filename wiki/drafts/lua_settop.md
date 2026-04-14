---
title: lua_settop
category: entities
created: 2026-04-14T13:47:59.805066+00:00
status: draft
---

# lua_settop

**Type**: Function  
**Module**: [[lua]]  

## Signature
```lua
void lua_settop (lua_State *L, int index);
```

## Description
Receives any acceptable stack index, or 0, and sets the stack top to this index. If the new top is greater than the old one, then the new elements are filled with **nil**. If `index` is 0, then all stack elements are removed.

## Parameters
_None_

## Returns
_None_

## Implementation Code
```c
void lua_settop (lua_State *L, int index);
```
