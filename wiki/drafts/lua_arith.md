---
title: lua_arith
category: entities
created: 2026-04-14T13:30:40.687067+00:00
status: draft
---

# lua_arith

**Type**: Function  
**Module**: [[lua]]  

## Signature
```lua
void lua_arith (lua_State *L, int op)
```

## Description
Performs an arithmetic or bitwise operation over the two values (or one, in the case of negations) at the top of the stack, with the value on the top being the second operand, pops these values, and pushes the result of the operation. The function follows the semantics of the corresponding Lua operator (that is, it may call metamethods).

## Parameters
_None_

## Returns
_None_

## Implementation Code
```c
void lua_arith (lua_State *L, int op);
```
