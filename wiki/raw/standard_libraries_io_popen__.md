# io.popen()

**Category**: Standard Libraries

### `io.popen (prog [, mode])`

This function is system dependent and is not available on all platforms.

Starts the program `prog` in a separated process and returns a file handle that you can use to read data from this program (if `mode` is `"r"`, the default) or to write data to this program (if `mode` is `"w"`).