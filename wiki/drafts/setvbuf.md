---
title: setvbuf
category: entities
created: 2026-04-14T20:11:42.592975+00:00
status: draft
---

# setvbuf

**Type**: Function  
**Module**: [[file]]  

## Signature
```lua
void file:setvbuf (mode, size)
```

## Description
Sets the buffering mode for a file. There are three available modes: no, full, line. For the last two cases, size is a hint for the size of the buffer, in bytes. The default is an appropriate size.

## Parameters
- `mode` (string): The buffering mode: no, full, line.
- `size` (integer): A hint for the size of the buffer, in bytes. The default is an appropriate size.

## Returns
- (void): No return value.

## Implementation Code
```c
void file:setvbuf (mode, size)
```
