---
title: luaL_buffinitsize
category: entities
created: 2026-04-14T16:43:09.353522+00:00
status: draft
---

# luaL_buffinitsize

**Type**: Function  
**Module**: [[auxiliary library]]  

## Signature
```lua
char *luaL_buffinitsize (lua_State *L, luaL_Buffer *B, size_t sz)
```

## Description
Initializes a buffer for a given size.

## Parameters
_None_

## Returns
- (char *): A pointer to the initialized buffer.

## Implementation Code
```c
char *luaL_buffinitsize (lua_State *L, luaL_Buffer *B, size_t sz)
```
