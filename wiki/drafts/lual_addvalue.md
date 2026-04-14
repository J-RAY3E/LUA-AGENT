---
title: luaL_addvalue
category: entities
created: 2026-04-14T15:45:51.810971+00:00
status: draft
---

# luaL_addvalue

**Type**: Function  
**Module**: [[auxiliary library]]  

## Signature
```lua
void luaL_addvalue (luaL_Buffer *B)
```

## Description
Adds the value on the top of the stack to the buffer B (see [luaL_Buffer](#luaL_Buffer)). Pops the value.

## Parameters
_None_

## Returns
_None_

## Implementation Code
```c
void luaL_addvalue (luaL_Buffer *B)
```
