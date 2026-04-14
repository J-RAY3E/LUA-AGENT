# string.dump()

**Category**: Standard Libraries

### `string.dump (function [, strip])`

Returns a string containing a binary representation (a *binary chunk*) of the given function, so that a later [`load`](#pdf-load) on this string returns a copy of the function (but with new upvalues). If `strip` is a true value, the binary representation may not include all debug information about the function, to save space.

Functions with upvalues have only their number of upvalues saved. When (re)loaded, those upvalues receive fresh instances. (See the [`load`](#pdf-load) function for details about how these upvalues are initialized. You can use the debug library to serialize and reload the upvalues of a function in a way adequate to your needs.)