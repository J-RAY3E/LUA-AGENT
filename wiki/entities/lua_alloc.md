---
title: lua_Alloc
category: entities
created: 2026-04-14T10:36:27.850556+00:00
status: published
---

# lua_Alloc

**Type**: Function  
**Module**: [[lua]]  

## Signature
```lua
void * (*lua_Alloc) (void *ud, void *ptr, size_t osize, size_t nsize)
```

## Description
The type of the memory-allocator function used by Lua states. The allocator function must provide a functionality similar to `realloc`, but not exactly the same. Its arguments are `ud`, an opaque pointer passed to [`lua_newstate`](#lua_newstate); `ptr`, a pointer to the block being allocated/reallocated/freed; `osize`, the original size of the block or some code about what is being allocated; and `nsize`, the new size of the block.

## Parameters
_None_

## Returns
- (void *): The memory allocated or reallocated.

## Implementation Code
```c
typedef void * (*lua_Alloc) (void *ud, void *ptr, size_t osize, size_t nsize);
```
