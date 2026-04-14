# utf8.len()

**Category**: Standard Libraries

### `utf8.len (s [, i [, j [, lax]]])`

Returns the number of UTF-8 characters in string `s` that start between positions `i` and `j` (both inclusive). The default for `i` is 1 and for `j` is -1. If it finds any invalid byte sequence, returns **fail** plus the position of the first invalid byte.