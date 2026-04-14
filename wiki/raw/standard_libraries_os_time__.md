# os.time()

**Category**: Standard Libraries

### `os.time ([table])`

Returns the current local time when called without arguments, or a time representing the local date and time specified by the given table. This table must have fields `year`, `month`, and `day`, and may have fields `hour` (default is 12), `min` (default is 0), `sec` (default is 0), and `isdst` (default is **nil**). Other fields are ignored. For a description of these fields, see the [`os.date`](#pdf-os.date) function.

When the function is called, the values in these fields do not need to be inside their valid ranges. For instance, if `sec` is -10, it means 10 seconds before the time specified by the other fields; if `hour` is 1000, it means 1000 hours after the time specified by the other fields.

The returned value is a number, whose meaning depends on your system. In POSIX, Windows, and some other systems, this number counts the number of seconds since some given start time (the "epoch"). In other systems, the meaning is not specified, and the number returned by `time` can be used only as an argument to [`os.date`](#pdf-os.date) and [`os.difftime`](#pdf-os.difftime).

When called with a table, `os.time` also normalizes all the fields documented in the [`os.date`](#pdf-os.date) function, so that they represent the same time as before the call but with values inside their valid ranges.