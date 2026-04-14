---
title: ipairs
category: entities
created: 2026-04-14T21:13:52.519302+00:00
status: published
---

# ipairs

**Type**: Function  
**Module**: [[Standard Libraries]]  

## Signature
```lua
t
```

## Description
Returns three values (an iterator function, the value `t`, and 0) so that the construction

lua
for i, v in ipairs(t) do body end

will iterate over the key–value pairs (`1, t[1]`), (`2, t[2]`), ..., up to the first absent index.

## Parameters
_None_

## Returns
- (function): an iterator function
- (value): the value `t`
- (integer): 0

## Implementation Code
```c

```
