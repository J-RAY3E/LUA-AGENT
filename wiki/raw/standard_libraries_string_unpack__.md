# string.unpack()

**Category**: Standard Libraries

### `string.unpack (fmt, s [, pos])`

Returns the values packed in string `s` (see [`string.pack`](#pdf-string.pack)) according to the format string `fmt` (see [§6.5.2](#6.5.2)). An optional `pos` marks where to start reading in `s` (default is 1). After the read values, this function also returns the index of the first unread byte in `s`.