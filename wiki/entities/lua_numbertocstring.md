---
title: lua_numbertocstring
category: entities
created: 2026-04-14T13:40:48.567808+00:00
status: published
---

# lua_numbertocstring

**Type**: Function  
**Module**: [[lua]]  

## Signature
```lua
unsigned lua_numbertocstring (lua_State *L, int idx, char *buff)
```

## Description
Converts the number at acceptable index `idx` to a string and puts the result in `buff`. The buffer must have a size of at least `LUA_N2SBUFFSZ` bytes. The conversion follows a non-specified format (see §3.4.3). The function returns the number of bytes written to the buffer (including the final zero), or zero if the value at `idx` is not a number.

## Parameters
- `L` (lua_State*): lua_State*
- `idx` (int): index
- `buff` (char*): buffer

## Returns
- (unsigned): number of bytes written to the buffer (including the final zero)

## Implementation Code
```c
unsigned lua_numbertocstring (lua_State *L, int idx, char *buff)
```
