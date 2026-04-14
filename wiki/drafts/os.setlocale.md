---
title: os.setlocale
category: entities
created: 2026-04-14T21:20:25.045910+00:00
status: draft
---

# os.setlocale

**Type**: Function  
**Module**: [[Standard Libraries]]  

## Signature
```lua
os.setlocale(locale, category)
```

## Description
Sets the current locale of the program. `locale` is a system-dependent string specifying a locale; `category` is an optional string describing which category to change: "all", "collate", "ctype", "monetary", "numeric", or "time"; the default category is "all". The function returns the name of the new locale, or "fail" if the request cannot be honored.

## Parameters
_None_

## Returns
- (string): The name of the new locale, or "fail" if the request cannot be honored.

## Implementation Code
```c
lua_Alloc, lua_State, lua_Number, etc.
```
