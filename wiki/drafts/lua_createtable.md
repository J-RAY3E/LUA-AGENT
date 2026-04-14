---
title: lua_createtable
category: entities
created: 2026-04-14T10:50:25.884263+00:00
status: draft
---

# lua_createtable

**Type**: Function  
**Module**: [[lua]]  

## Signature
```lua
void lua_createtable (lua_State *L, int nseq, int nrec);
```

## Description
Creates a new empty table and pushes it onto the stack. Parameter `nseq` is a hint for how many elements the table will have as a sequence; parameter `nrec` is a hint for how many other elements the table will have. Lua may use these hints to preallocate memory for the new table. This preallocation may help performance when you know in advance how many elements the table will have. Otherwise you should use the function [`lua_newtable`](#lua_newtable).

## Parameters
- `L` (lua_State *): The Lua state to operate on.
- `nseq` (int): A hint for how many elements the table will have as a sequence.
- `nrec` (int): A hint for how many other elements the table will have.

## Returns
- (void): No return value.

## Implementation Code
```c

```
