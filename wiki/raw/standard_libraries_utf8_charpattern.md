# utf8.charpattern

**Category**: Standard Libraries

### `utf8.charpattern`

The pattern (a string, not a function) "`[\0-\x7F\xC2-\xFD][\x80-\xBF]*`" (see [§6.5.1](#6.5.1)), which matches exactly one UTF-8 byte sequence, assuming that the subject is a valid UTF-8 string.