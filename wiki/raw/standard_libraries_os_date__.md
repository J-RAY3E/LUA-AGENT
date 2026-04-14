# os.date()

**Category**: Standard Libraries

### `os.date ([format [, time]])`

Returns a string or a table containing date and time, formatted according to the given string `format`.

If the `time` argument is present, this is the time to be formatted (see the [`os.time`](#pdf-os.time) function for a description of this value). Otherwise, `date` formats the current time.

If `format` starts with '`!`', then the date is formatted in Coordinated Universal Time. After this optional character, if `format` is the string "`*t`", then `date` returns a table with the following fields: `year`, `month` (1–12), `day` (1–31), `hour` (0–23), `min` (0–59), `sec` (0–61, due to leap seconds), `wday` (weekday, 1–7, Sunday is 1), `yday` (day of the year, 1–366), and `isdst` (daylight saving flag, a boolean). This last field may be absent if the information is not available.

If `format` is not "`*t`", then `date` returns the date as a string, formatted according to the same rules as the ISO C function `strftime`.

If `format` is absent, it defaults to "`%c`", which gives a human-readable date and time representation using the current locale.

On non-POSIX systems, this function may be not thread safe because of its reliance on C function `gmtime` and C function `localtime`.