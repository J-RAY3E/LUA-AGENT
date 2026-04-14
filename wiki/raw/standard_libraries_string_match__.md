# string.match()

**Category**: Standard Libraries

### `string.match (s, pattern [, init])`

Looks for the first *match* of the `pattern` (see [§6.5.1](#6.5.1)) in the string `s`. If it finds one, then `match` returns the captures from the pattern; otherwise it returns **fail**. If `pattern` specifies no captures, then the whole match is returned. A third, optional numeric argument `init` specifies where to start the search; its default value is 1 and can be negative.