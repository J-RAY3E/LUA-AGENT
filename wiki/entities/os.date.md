---
title: os.date
category: entities
created: 2026-04-14T21:19:18.408560+00:00
status: published
---

# os.date

**Type**: Function  
**Module**: [[Standard Libraries]]  

## Signature
```lua
os.date([format, time])
```

## Description
Returns a string or a table containing date and time, formatted according to the given string `format`. If the `time` argument is present, this is the time to be formatted (see the `os.time` function for a description of this value). Otherwise, `date` formats the current time.

## Parameters
- `format` (string): The format string for the date and time. If the `time` argument is present, this is the time to be formatted (see the `os.time` function for a description of this value). Otherwise, `date` formats the current time.
- `time` (number): The time to be formatted. If the `format` argument is present, this is the time to be formatted (see the `os.time` function for a description of this value). Otherwise, `date` formats the current time.

## Returns
- (string): The formatted date and time as a string.
- (table): A table containing the following fields: `year`, `month` (1–12), `day` (1–31), `hour` (0–23), `min` (0–59), `sec` (0–61, due to leap seconds), `wday` (weekday, 1–7, Sunday is 1), `yday` (day of the year, 1–366), and `isdst` (daylight saving flag, a boolean). This last field may be absent if the information is not available.

## Implementation Code
```c
os.date([format, time])
```
