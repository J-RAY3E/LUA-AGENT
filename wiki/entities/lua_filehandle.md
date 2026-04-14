---
title: LUA_FILEHANDLE
category: entities
created: 2026-04-14T17:11:09.722712+00:00
status: published
---

# LUA_FILEHANDLE

**Type**: Constant  

## Value
```c
typedef struct luaL_Stream { FILE *f; lua_CFunction closef; } luaL_Stream;
```

## Description
The name of the metatable for file handles.
