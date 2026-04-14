# string.find()

**Category**: Standard Libraries

### `string.find (s, pattern [, init [, plain]])`

Looks for the first match of `pattern` (see [§6.5.1](#6.5.1)) in the string `s`. If it finds a match, then `find` returns the indices of `s` where this occurrence starts and ends; otherwise, it returns **fail**. A third, optional numeric argument `init` specifies where to start the search; its default value is 1 and can be negative. A **true** as a fourth, optional argument `plain` turns off the pattern matching facilities, so the function does a plain "find substring" operation, with no characters in `pattern` being considered magic.

If the pattern has captures, then in a successful match the captured values are also returned, after the two indices.