---
title: luaL_pushresult
category: entities
created: 2026-04-14T16:51:04.526601+00:00
status: published
---

# luaL_pushresult

**Type**: Function  
**Module**: [[auxiliary library]]  

## Signature
```lua
void luaL_pushresult (luaL_Buffer *B)
```

## Description
Finishes the use of buffer `B` leaving the final string on the top of the stack.

## Parameters
_None_

## Returns
_None_

## Implementation Code
```c
void luaL_pushresult (luaL_Buffer *B)
```
