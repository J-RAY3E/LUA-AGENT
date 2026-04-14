---
title: lua_WarnFunction
category: entities
created: 2026-04-14T13:52:15.682154+00:00
status: draft
---

# lua_WarnFunction

**Type**: Function  
**Module**: [[lua]]  

## Signature
```lua
void (*lua_WarnFunction)(void *ud, const char *msg, int tocont)
```

## Description
The type of warning functions, called by Lua to emit warnings. The first parameter is an opaque pointer set by `lua_setwarnf`. The second parameter is the warning message. The third parameter is a boolean that indicates whether the message is to be continued by the message in the next call.

## Parameters
_None_

## Returns
_None_

## Implementation Code
```c
typedef void (*lua_WarnFunction)(void *ud, const char *msg, int tocont);
```
