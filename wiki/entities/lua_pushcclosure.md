---
title: lua_pushcclosure
category: entities
created: 2026-04-14T13:41:54.929546+00:00
status: published
---

# lua_pushcclosure

**Type**: Function  
**Module**: [[lua]]  

## Signature
```lua
void lua_pushcclosure (lua_State *L, lua_CFunction fn, int n)
```

## Description
Pushes a new C closure onto the stack. This function receives a pointer to a C function and pushes onto the stack a Lua value of type function that, when called, invokes the corresponding C function. The parameter n tells how many upvalues this function will have (see §4.2).

## Parameters
- `L` (lua_State *): Pointer to the Lua state
- `fn` (lua_CFunction): Pointer to the C function
- `n` (int): Number of upvalues

## Returns
- (void): No return value

## Implementation Code
```c
void lua_pushcclosure (lua_State *L, lua_CFunction fn, int n)
```
