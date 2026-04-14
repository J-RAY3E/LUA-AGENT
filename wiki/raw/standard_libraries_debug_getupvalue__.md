# debug.getupvalue()

**Category**: Standard Libraries

### `debug.getupvalue (f, up)`

This function returns the name and the value of the upvalue with index `up` of the function `f`. The function returns **fail** if there is no upvalue with the given index.

(For Lua functions, upvalues are the external local variables that the function uses, and that are consequently included in its closure.)

For C functions, this function uses the empty string `""` as a name for all upvalues.

Variable name '`?`' (interrogation mark) represents variables with no known names (variables from chunks saved without debug information).