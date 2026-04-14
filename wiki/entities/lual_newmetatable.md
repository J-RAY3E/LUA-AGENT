---
title: luaL_newmetatable
category: entities
created: 2026-04-14T17:11:09.720247+00:00
status: published
---

# luaL_newmetatable

**Type**: API Type (typedef)  

## Definition
```c
typedef struct luaL_Stream { FILE *f; lua_CFunction closef; } luaL_Stream;
```

## Description
Creates a metatable for a given type.
