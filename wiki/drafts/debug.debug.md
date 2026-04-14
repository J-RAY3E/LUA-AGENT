---
title: debug.debug
category: entities
created: 2026-04-14T20:07:45.360689+00:00
status: draft
---

# debug.debug

**Type**: Function  
**Module**: [[Standard Libraries]]  

## Signature
```lua
void
```

## Description
Enters an interactive mode with the user, running each string that the user enters. Using simple commands and other debug facilities, the user can inspect global and local variables, change their values, evaluate expressions, and so on. A line containing only the word `cont` finishes this function, so that the caller continues its execution.

## Parameters
_None_

## Returns
_None_

## Implementation Code
```c
void debug_debug(void) {}
```
