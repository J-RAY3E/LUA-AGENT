---
title: error
category: entities
created: 2026-04-14T20:10:42.421425+00:00
status: published
---

# error

**Type**: Function  
**Module**: [[Standard Libraries]]  

## Signature
```lua
message (level)
```

## Description
Adds some information about the error position at the beginning of the message. The `level` argument specifies how to get the error position. With level 1 (the default), the error position is where the `error` function was called. Level 2 points the error to where the function that called `error` was called; and so on. Passing a level 0 avoids the addition of error position information to the message.

## Parameters
- `message` (string): Usually, `error` adds some information about the error position at the beginning of the message.
- `level` (number): Usually, `error` adds some information about the error position at the beginning of the message. The `level` argument specifies how to get the error position. With level 1 (the default), the error position is where the `error` function was called. Level 2 points the error to where the function that called `error` was called; and so on. Passing a level 0 avoids the addition of error position information to the message.

## Returns
- (string): Usually, `error` adds some information about the error position at the beginning of the message. The `level` argument specifies how to get the error position. With level 1 (the default), the error position is where the `error` function was called. Level 2 points the error to where the function that called `error` was called; and so on. Passing a level 0 avoids the addition of error position information to the message.

## Implementation Code
```c
error(message, level)
```
