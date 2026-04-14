# file:write()

**Category**: Standard Libraries

### `file:write (···)`

Writes the value of each of its arguments to `file`. The arguments must be strings or numbers.

In case of success, this function returns `file`. Otherwise, it returns four values: **fail**, the error message, the error code, and the number of bytes it was able to write.