---
title: os.difftime
category: entities
created: 2026-04-14T21:19:27.386868+00:00
status: published
---

# os.difftime

**Type**: Function  
**Module**: [[Standard Libraries]]  

## Signature
```lua
t2, t1
```

## Description
Returns the difference, in seconds, from time t1 to time t2 (where the times are values returned by os.time). In POSIX, Windows, and some other systems, this value is exactly t2 - t1.

## Parameters
_None_

## Returns
- (lua_Number): The difference in seconds between t2 and t1.

## Implementation Code
```c
t2, t1
```
