---
title: os.exit
category: entities
created: 2026-04-14T21:19:50.623022+00:00
status: published
---

# os.exit

**Type**: Function  
**Module**: [[Standard Libraries]]  

## Signature
```lua
void os.exit([bool code, bool close])
```

## Description
Calls the ISO C function `exit` to terminate the host program. If `code` is `true`, the returned status is `EXIT_SUCCESS`; if `code` is `false`, the returned status is `EXIT_FAILURE`; if `code` is a number, the returned status is this number. The default value for `code` is `true`. If the optional second argument `close` is `true`, the function closes the Lua state before exiting (see [`lua_close`](#lua_close)).

## Parameters
- `code` (bool): If `true`, the returned status is `EXIT_SUCCESS`; if `false`, the returned status is `EXIT_FAILURE`; if `code` is a number, the returned status is this number. The default value for `code` is `true`. 
- `close` (bool): If `true`, the function closes the Lua state before exiting.

## Returns
- (void): None

## Implementation Code
```c
void os.exit([bool code, bool close])
```
