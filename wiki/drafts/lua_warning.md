---
title: lua_warning
category: entities
created: 2026-04-14T13:52:25.248540+00:00
status: draft
---

# lua_warning

**Type**: Function  
**Module**: [[lua]]  

## Signature
```lua
void lua_warning (lua_State *L, const char *msg, int tocont)
```

## Description
Emits a warning with the given message. A message in a call with `tocont` true should be continued in another call to this function.

## Parameters
- `L` (lua_State*): lua_State*
- `msg` (const char*): message
- `tocont` (int): true if message should be continued in another call

## Returns
_None_

## Implementation Code
```c
void lua_warning (lua_State *L, const char *msg, int tocont)
```
