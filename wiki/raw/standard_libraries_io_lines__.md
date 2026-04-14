# io.lines()

**Category**: Standard Libraries

### `io.lines ([filename, ···])`

Opens the given file name in read mode and returns an iterator function that works like `file:lines(···)` over the opened file. When the iterator function fails to read any value, it automatically closes the file. Besides the iterator function, `io.lines` returns three other values: two **nil** values as placeholders, plus the created file handle. Therefore, when used in a generic **for** loop, the file is closed also if the loop is interrupted by an error or a **break**.

The call `io.lines()` (with no file name) is equivalent to `io.input():lines("l")`; that is, it iterates over the lines of the default input file. In this case, the iterator does not close the file when the loop ends.

In case of errors opening the file, this function raises the error, instead of returning an error code.