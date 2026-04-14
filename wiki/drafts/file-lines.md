---
title: file:lines
category: entities
created: 2026-04-14T20:11:06.562564+00:00
status: draft
---

# file:lines

**Type**: Function  
**Module**: [[file]]  

## Signature
```lua
function (self, formats)
```

## Description
Returns an iterator function that, each time it is called, reads the file according to the given formats. When no format is given, uses `l` as a default. As an example, the construction
lua
for c in file:lines(1) do body end

will iterate over all characters of the file, starting at the current position. Unlike `io.lines`, this function does not close the file when the loop ends.

## Parameters
- `formats` (table): An optional table of formats to use for reading the file. If not provided, `l` is used as a default format.

## Returns
- (function): An iterator function that, each time it is called, reads the file according to the given formats.

## Implementation Code
```c
function (self, formats)
  -- implementation details
end
```
