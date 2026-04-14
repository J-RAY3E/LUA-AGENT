---
title: lua_dump
category: entities
created: 2026-04-14T10:50:59.014031+00:00
status: draft
---

# lua_dump

**Type**: Function  
**Module**: [[lua]]  

## Signature
```lua
int lua_dump (lua_State *L, lua_Writer writer, void *data, int strip)
```

## Description
Dumps a function as a binary chunk. Receives a Lua function on the top of the stack and produces a binary chunk that, if loaded again, results in a function equivalent to the one dumped. As it produces parts of the chunk, `lua_dump` calls function `writer` (see `lua_Writer`) with the given `data` to write them.

## Parameters
- `L` (lua_State*): Lua state
- `writer` (lua_Writer): Writer function
- `data` (void*): Data for the writer function
- `strip` (int): Whether to strip debug information

## Returns
- (int): Error code returned by the last call to the writer

## Implementation Code
```c
int lua_dump (lua_State *L, lua_Writer writer, void *data, int strip)
```
