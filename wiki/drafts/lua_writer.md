---
title: lua_Writer
category: entities
created: 2026-04-14T13:52:39.263615+00:00
status: draft
---

# lua_Writer

**Type**: Function  
**Module**: [[lua]]  

## Signature
```lua
int (*lua_Writer)(lua_State *L, const void* p, size_t sz, void* ud)
```

## Description
The type of the writer function used by `lua_dump`. Every time `lua_dump` produces another piece of chunk, it calls the writer, passing along the buffer to be written (`p`), its size (`sz`), and the `ud` parameter supplied to `lua_dump`. After `lua_dump` writes its last piece, it will signal that by calling the writer function one more time, with a `NULL` buffer (and size 0). The writer returns an error code: 0 means no errors; any other value means an error and stops `lua_dump` from calling the writer again.

## Parameters
- `L` (lua_State*): The Lua state to operate on.
- `p` (const void*): The buffer to be written.
- `sz` (size_t): The size of the buffer.
- `ud` (void*): The user data passed to `lua_dump`.

## Returns
- (int): The error code. 0 means no errors; any other value means an error and stops `lua_dump` from calling the writer again.

## Implementation Code
```c
typedef int (*lua_Writer)(lua_State *L, const void* p, size_t sz, void* ud)
```
