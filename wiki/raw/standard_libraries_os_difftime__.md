# os.difftime()

**Category**: Standard Libraries

### `os.difftime (t2, t1)`

Returns the difference, in seconds, from time `t1` to time `t2` (where the times are values returned by [`os.time`](#pdf-os.time)). In POSIX, Windows, and some other systems, this value is exactly `t2`*-*`t1`.