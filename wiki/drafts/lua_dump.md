---
title: lua_dump
category: entities
created: 2026-04-14T13:33:16.152046+00:00
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
- `L` (lua_State*): The Lua state to operate on.
- `writer` (lua_Writer): A function to write the binary chunk.
- `data` (void*): Data to pass to the writer function.
- `strip` (int): If true, the binary representation may not include all debug information about the function, to save space.

## Returns
- (int): The error code returned by the last call to the writer; 0 means no errors.

## Implementation Code
```c
int lua_dump (lua_State *L, lua_Writer writer, void *data, int strip)
```
