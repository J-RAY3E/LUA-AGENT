---
title: lua_concat
category: entities
created: 2026-04-14T13:32:23.985134+00:00
status: published
---

# lua_concat

**Type**: Function  
**Module**: [[lua]]  

## Signature
```lua
void lua_concat (lua_State *L, int n)
```

## Description
Concatenates the n values at the top of the stack, pops them, and leaves the result on the top. If n is 1, the result is the single value on the stack (that is, the function does nothing); if n is 0, the result is the empty string. Concatenation is performed following the usual semantics of Lua (see §3.4.6).

## Parameters
_None_

## Returns
_None_

## Implementation Code
```c
void lua_concat (lua_State *L, int n)
```
