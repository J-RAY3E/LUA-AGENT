---
title: lua_closethread
category: entities
created: 2026-04-14T13:32:02.966112+00:00
status: published
---

# lua_closethread

**Type**: Function  
**Module**: [[lua]]  

## Signature
```lua
int lua_closethread (lua_State *L, lua_State *from)
```

## Description
Resets a thread, cleaning its call stack and closing all pending to-be-closed variables. The parameter `from` represents the coroutine that is resetting `L`. If there is no such coroutine, this parameter can be `NULL`. Unless `L` is equal to `from`, the call returns a status code: `LUA_OK` for no errors in the thread (either the original error that stopped the thread or errors in closing methods), or an error status otherwise. In case of error, the error object is put on the top of the stack.

## Parameters
- `L` (lua_State*): The Lua state to reset.
- `from` (lua_State*): The coroutine that is resetting `L`. If there is no such coroutine, this parameter can be `NULL`.

## Returns
- (int): Status code. `LUA_OK` for no errors in the thread, or an error status otherwise. In case of error, the error object is put on the top of the stack.

## Implementation Code
```c
int lua_closethread (lua_State *L, lua_State *from)
```
