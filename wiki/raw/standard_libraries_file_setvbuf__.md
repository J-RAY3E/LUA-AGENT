# file:setvbuf()

**Category**: Standard Libraries

### `file:setvbuf (mode [, size])`

Sets the buffering mode for a file. There are three available modes:

* "`no`": no buffering.
* "`full`": full buffering.
* "`line`": line buffering.

For the last two cases, `size` is a hint for the size of the buffer, in bytes. The default is an appropriate size.

The specific behavior of each mode is non portable; check the underlying ISO C function `setvbuf` in your platform for more details.