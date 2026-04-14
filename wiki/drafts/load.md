---
title: load
category: entities
created: 2026-04-14T21:14:06.042956+00:00
status: draft
---

# load

**Type**: Function  
**Module**: [[Standard Libraries]]  

## Signature
```lua
load(chunk [, chunkname [, mode [, env]]])
```

## Description
Loads a chunk.

## Parameters
- `chunk` (string): The chunk to load.
- `chunkname` (string): The name of the chunk for error messages and debug information.
- `mode` (string): Controls whether the chunk can be text or binary.
- `env` (any): The environment to use for the chunk.

## Returns
- (function): The compiled chunk as a function.
- (string): The error message if there are syntactic errors.

## Implementation Code
```c
load(chunk [, chunkname [, mode [, env]]])
```
