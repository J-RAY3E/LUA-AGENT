---
title: lua_Reader
category: entities
created: 2026-04-14T13:45:31.271661+00:00
status: draft
---

# lua_Reader

**Type**: Function  
**Module**: [[lua]]  

## Signature
```lua
const char * (*lua_Reader) (lua_State *L, void *data, size_t *size)
```

## Description
The reader function used by `lua_load`. Every time `lua_load` needs another piece of the chunk, it calls the reader, passing along its `data` parameter. The reader must return a pointer to a block of memory with a new piece of the chunk and set `size` to the block size. The block must exist until the reader function is called again. To signal the end of the chunk, the reader must return `NULL` or set `size` to zero. The reader function may return pieces of any size greater than zero.

## Parameters
_None_

## Returns
- (const char *): A pointer to a block of memory with a new piece of the chunk.
- (void *): The data passed to the reader function.
- (size_t): The size of the block of memory returned by the reader function.

## Implementation Code
```c
typedef const char * (*lua_Reader) (lua_State *L, void *data, size_t *size)
```
