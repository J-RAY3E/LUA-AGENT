---
title: C-call boundary
category: concepts
created: 2026-04-14T13:53:13.390466+00:00
status: published
---

# C-call boundary

**Type**: Concept  

## Overview
A boundary in a Lua thread where a C function call is made without a continuation function.

## Implementation / Context Code
```lua
int lua_yieldk (lua_State *L, int nresults, lua_KContext ctx, lua_KFunction k)
```

## Related Concepts
_None_

## Related Modules
_None_

## Notes
_Auto-generated from source: api_lua_yieldk.md_
