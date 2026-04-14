---
title: luaL_openselectedlibs
category: entities
created: 2026-04-14T21:14:37.844087+00:00
status: published
---

# luaL_openselectedlibs

**Type**: Function  
**Module**: [[lua]]  

## Signature
```lua
void luaL_openselectedlibs (lua_State *L, int load, int preload)
```

## Description
Opens (loads) and preloads selected standard libraries into the state `L`. (To *preload* means to add the library loader into the table [`package.preload`](#pdf-package.preload), so that the library can be required later by the program. Keep in mind that [`require`](#pdf-require) itself is provided by the *package* library. If a program does not load that library, it will be unable to require anything.)

## Parameters
- `L` (lua_State*): The Lua state to operate on.
- `load` (int): A mask formed by a bitwise OR of the following constants: `LUA_GLIBK`, `LUA_LOADLIBK`, `LUA_COLIBK`, `LUA_STRLIBK`, `LUA_UTF8LIBK`, `LUA_TABLIBK`, `LUA_MATHLIBK`, `LUA_IOLIBK`, `LUA_OSLIBK`, `LUA_DBLIBK`.
- `preload` (int): A mask formed by a bitwise OR of the following constants: `LUA_GLIBK`, `LUA_LOADLIBK`, `LUA_COLIBK`, `LUA_STRLIBK`, `LUA_UTF8LIBK`, `LUA_TABLIBK`, `LUA_MATHLIBK`, `LUA_IOLIBK`, `LUA_OSLIBK`, `LUA_DBLIBK`.

## Returns
- (void): None

## Implementation Code
```c
void luaL_openselectedlibs (lua_State *L, int load, int preload)
```
