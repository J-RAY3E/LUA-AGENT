# debug.getinfo()

**Category**: Standard Libraries

### `debug.getinfo ([thread,] f [, what])`

Returns a table with information about a function. You can give the function directly or you can give a number as the value of `f`, which means the function running at level `f` of the call stack of the given thread: level 0 is the current function (`getinfo` itself); level 1 is the function that called `getinfo` (except for tail calls, which do not count in the stack); and so on. If `f` is a number greater than the number of active functions, then `getinfo` returns **fail**.

The returned table can contain all the fields returned by [`lua_getinfo`](#lua_getinfo), with the string `what` describing which fields to fill in. The default for `what` is to get all information available, except the table of valid lines. The option '`f`' adds a field named `func` with the function itself. The option '`L`' adds a field named `activelines` with the table of valid lines, provided the function is a Lua function. If the function has no debug information, the table is empty.

For instance, the expression `debug.getinfo(1,"n").name` returns a name for the current function, if a reasonable name can be found, and the expression `debug.getinfo(print)` returns a table with all available information about the [`print`](#pdf-print) function.