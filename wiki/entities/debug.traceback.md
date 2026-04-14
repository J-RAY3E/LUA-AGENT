---
title: debug.traceback
category: entities
created: 2026-04-14T20:10:00.760048+00:00
status: published
---

# debug.traceback

**Type**: Function  
**Module**: [[Standard Libraries]]  

## Signature
```lua
debug.traceback([thread,] [message [, level]])
```

## Description
If `message` is present but is neither a string nor **nil**, this function returns `message` without further processing. Otherwise, it returns a string with a traceback of the call stack. The optional `message` string is appended at the beginning of the traceback. An optional `level` number tells at which level to start the traceback (default is 1, the function calling `traceback`).

## Parameters
_None_

## Returns
- (string): A string with a traceback of the call stack.

## Implementation Code
```c
lua_Alloc, lua_State, lua_Number, etc.
```
