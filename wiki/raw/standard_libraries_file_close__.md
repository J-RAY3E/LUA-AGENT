# file:close()

**Category**: Standard Libraries

### `file:close ()`

Closes `file`. Note that files are automatically closed when their handles are garbage collected, but that takes an unpredictable amount of time to happen.

When closing a file handle created with [`io.popen`](#pdf-io.popen), [`file:close`](#pdf-file:close) returns the same values returned by [`os.execute`](#pdf-os.execute).