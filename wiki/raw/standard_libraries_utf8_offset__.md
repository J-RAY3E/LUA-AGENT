# utf8.offset()

**Category**: Standard Libraries

### `utf8.offset (s, n [, i])`

Returns the position of the `n`-th character of `s` (counting from byte position `i`) as two integers: The index (in bytes) where its encoding starts and the index (in bytes) where it ends.

If the specified character is right after the end of `s`, the function behaves as if there was a '`\0`' there. If the specified character is neither in the subject nor right after its end, the function returns **fail**.

A negative `n` gets characters before position `i`. The default for `i` is 1 when `n` is non-negative and `#s + 1` otherwise, so that `utf8.offset(s,-n)` gets the offset of the `n`-th character from the end of the string.

As a special case, when `n` is 0 the function returns the start and end of the encoding of the character that contains the `i`-th byte of `s`.

This function assumes that `s` is a valid UTF-8 string.