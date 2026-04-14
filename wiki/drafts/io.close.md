---
title: io.close
category: entities
created: 2026-04-14T20:12:24.222897+00:00
status: draft
---

# io.close

**Type**: Function  
**Module**: [[Standard Libraries]]  

## Signature
```lua
void io.close([file])
```

## Description
Equivalent to `file:close()`. Without a `file`, closes the default output file.

## Parameters
_None_

## Returns
_None_

## Implementation Code
```c
void io_close(file) {
  if (file) file:close();
}

```
