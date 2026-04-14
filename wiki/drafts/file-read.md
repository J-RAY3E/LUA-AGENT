---
title: file:read
category: entities
created: 2026-04-14T20:11:18.424640+00:00
status: draft
---

# file:read

**Type**: Function  
**Module**: [[Standard Libraries]]  

## Signature
```lua
file:read (···)
```

## Description
Reads the file `file`, according to the given formats, which specify what to read. For each format, the function returns a string or a number with the characters read, or **fail** if it cannot read data with the specified format. (In this latter case, the function does not read subsequent formats.) When called without arguments, it uses a default format that reads the next line (see below).

## Parameters
_None_

## Returns
- (string): A string or a number with the characters read.
- (number): A number with the characters read.
- (string): A string with the characters read.
- (string): A string with the characters read.
- (string): A string with the characters read.

## Implementation Code
```c
file:read (···)
```
