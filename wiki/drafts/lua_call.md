---
title: lua_call
category: entities
created: 2026-04-14T10:48:36.230507+00:00
status: draft
---

# lua_call

**Type**: Function  
**Module**: [[lua]]  

## Signature
```lua
void lua_call (lua_State *L, int nargs, int nresults)
```

## Description
Calls a function. Like regular Lua calls, `lua_call` respects the `__call` metamethod. So, here the word "function" means any callable value.

## Parameters
- `L` (lua_State*): lua_State* is a pointer to a Lua state.
- `nargs` (int): The number of arguments that you pushed onto the stack.
- `nresults` (int): The number of results that the function returns.

## Returns
- (void): No return value.

## Implementation Code
```c
void lua_call (lua_State *L, int nargs, int nresults)
```
