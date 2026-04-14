# utf8.codes()

**Category**: Standard Libraries

### `utf8.codes (s [, lax])`

Returns values so that the construction

```lua
for p, c in utf8.codes(s) do body end
```

will iterate over all UTF-8 characters in string `s`, with `p` being the position (in bytes) and `c` the code point of each character. It raises an error if it meets any invalid byte sequence.