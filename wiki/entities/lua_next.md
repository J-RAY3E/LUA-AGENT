---
title: lua_next
category: entities
created: 2026-04-14T13:40:27.770797+00:00
status: published
---

# lua_next

**Type**: Function  
**Module**: [[lua]]  

## Signature
```lua
int lua_next (lua_State *L, int index)
```

## Description
Pops a key from the stack, and pushes a key–value pair from the table at the given index, the "next" pair after the given key. If there are no more elements in the table, then `lua_next` returns 0 and pushes nothing.

## Parameters
- `L` (lua_State*): The Lua state to operate on.
- `index` (int): The index of the table to retrieve the next key-value pair from.

## Returns
- (int): Returns 0 if there are no more elements in the table, otherwise returns the number of elements in the table.

## Implementation Code
```c
int lua_next (lua_State *L, int index)
```
