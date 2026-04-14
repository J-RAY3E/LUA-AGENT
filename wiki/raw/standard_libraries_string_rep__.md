# string.rep()

**Category**: Standard Libraries

### `string.rep (s, n [, sep])`

Returns a string that is the concatenation of `n` copies of the string `s` separated by the string `sep`. The default value for `sep` is the empty string (that is, no separator). Returns the empty string if `n` is not positive.

(Note that it is very easy to exhaust the memory of your machine with a single call to this function.)