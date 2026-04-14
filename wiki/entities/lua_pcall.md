---
title: lua_pcall
category: entities
created: 2026-04-14T19:43:15.749571+00:00
status: published
---

# lua_pcall

**Type**: API Type (function)  

## Definition
```c
lua_pcall
```

## Description
Calls a given function in protected mode. Any error while running the function stops its execution, and control returns immediately to pcall, which returns a status code.
