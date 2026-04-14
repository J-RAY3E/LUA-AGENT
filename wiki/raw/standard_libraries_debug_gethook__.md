# debug.gethook()

**Category**: Standard Libraries

### `debug.gethook ([thread])`

Returns the current hook settings of the thread, as three values: the current hook function, the current hook mask, and the current hook count, as set by the [`debug.sethook`](#pdf-debug.sethook) function.

Returns **fail** if there is no active hook.