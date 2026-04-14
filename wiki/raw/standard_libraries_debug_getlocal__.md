# debug.getlocal()

**Category**: Standard Libraries

### `debug.getlocal ([thread,] f, local)`

This function returns the name and the value of the local variable with index `local` of the function at level `f` of the stack. This function accesses not only explicit local variables, but also parameters and temporary values.

The first parameter or local variable has index 1, and so on, following the order that they are declared in the code, counting only the variables that are active in the current scope of the function. Compile-time constants may not appear in this listing, if they were optimized away by the compiler. Negative indices refer to vararg arguments; -1 is the first vararg argument. These negative indices are only available when the vararg table has been optimized away; otherwise, the vararg arguments are available in the vararg table.

The function returns **fail** if there is no variable with the given index, and raises an error when called with a level out of range. (You can call [`debug.getinfo`](#pdf-debug.getinfo) to check whether the level is valid.)

Variable names starting with '`(`' (open parenthesis) represent variables with no known names (internal variables such as loop control variables, and variables from chunks saved without debug information).

The parameter `f` may also be a function. In that case, `getlocal` returns only the name of function parameters.