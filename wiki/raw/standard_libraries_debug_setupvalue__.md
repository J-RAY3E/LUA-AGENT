# debug.setupvalue()

**Category**: Standard Libraries

### `debug.setupvalue (f, up, value)`

This function assigns the value `value` to the upvalue with index `up` of the function `f`. The function returns **fail** if there is no upvalue with the given index. Otherwise, it returns the name of the upvalue.

See [`debug.getupvalue`](#pdf-debug.getupvalue) for more information about upvalues.