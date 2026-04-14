# utf8.codepoint()

**Category**: Standard Libraries

### `utf8.codepoint (s [, i [, j [, lax]]])`

Returns the code points (as integers) from all characters in `s` that start between byte position `i` and `j` (both included). The default for `i` is 1 and for `j` is `i`. It raises an error if it meets any invalid byte sequence.