---
title: lua_setupvalue
category: entities
created: 2026-04-14T13:48:12.459751+00:00
status: draft
---

# lua_setupvalue

**Type**: Function  
**Module**: [[lua]]  

## Signature
```lua
(lua_State *L, int funcindex, int n)
```

## Description
Sets the value of a closure's upvalue. It assigns the value on the top of the stack to the upvalue and returns its name. It also pops the value from the stack.

## Parameters
- `L` (lua_State*): lua_State* is a pointer to a Lua state.
- `funcindex` (int): Index of the function in the Lua state.
- `n` (int): Index of the upvalue in the function.

## Returns
- (const char*): Returns the name of the upvalue.

## Implementation Code
```c
const char *lua_setupvalue (lua_State *L, int funcindex, int n);
```
