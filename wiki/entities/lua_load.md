---
title: lua_load
category: entities
created: 2026-04-14T13:39:40.598954+00:00
status: published
---

# lua_load

**Type**: Function  
**Module**: [[lua]]  

## Signature
```lua
int lua_load(lua_State *L, lua_Reader reader, void *data, const char *chunkname, const char *mode)
```

## Description
Loads a Lua chunk without running it. If there are no errors, `lua_load` pushes the compiled chunk as a Lua function on top of the stack. Otherwise, it pushes an error message.

## Parameters
- `L` (lua_State *): The Lua state to operate on.
- `reader` (lua_Reader): A function to read the chunk.
- `data` (void *): An opaque value passed to the reader function.
- `chunkname` (const char *): A name to the chunk, used for error messages and in debug information.
- `mode` (const char *): A string that works as in function `load`, with the addition that a `NULL` value is equivalent to the string `"bt"`. Moreover, it may have a `"B"` instead of a `"b"`, meaning a *fixed buffer* with the binary dump.

## Returns
- (int): Returns `LUA_OK` if the chunk is successfully loaded, `LUA_ERRSYNTAX` if there are syntax errors, or `LUA_ERRMEM` if there is not enough memory.

## Implementation Code
```c
int lua_load (lua_State *L, lua_Reader reader, void *data, const char *chunkname, const char *mode);
```
