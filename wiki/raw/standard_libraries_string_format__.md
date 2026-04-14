# string.format()

**Category**: Standard Libraries

### `string.format (formatstring, ···)`

Returns a formatted version of its variable number of arguments following the description given in its first argument, which must be a string. The format string follows the same rules as the ISO C function `sprintf`. The accepted conversion specifiers are `A`, `a`, `c`, `d`, `E`, `e`, `f`, `G`, `g`, `i`, `o`, `p`, `s`, `u`, `X`, `x`, and '`%`', plus a non-C specifier `q`. The accepted flags are '`-`', '`+`', '`#`', '`0`', and '' (space). Both width and precision, when present, are limited to two digits.

The specifier `q` formats booleans, nil, numbers, and strings in a way that the result is a valid constant in Lua source code. Booleans and nil are written in the obvious way (`true`, `false`, `nil`). Floats are written in hexadecimal, to preserve full precision. A string is written between double quotes, using escape sequences when necessary to ensure that it can safely be read back by the Lua interpreter. For instance, the call

```lua
string.format('%q', 'a string with "quotes" and \n new line')
```

may produce the string:

```lua
"a string with \"quotes\" and \
 new line"
```

This specifier does not support modifiers (flags, width, precision).

The conversion specifiers `A`, `a`, `E`, `e`, `f`, `G`, and `g` all expect a number as argument. The specifiers `c`, `d`, `i`, `o`, `u`, `X`, and `x` expect an integer. When Lua is compiled with a C89 compiler, the specifiers `A` and `a` (hexadecimal floats) do not support modifiers.

The specifier `s` expects a string; if its argument is not a string, it is converted to one following the same rules of [`tostring`](#pdf-tostring). If the specifier has any modifier, the corresponding string argument should not contain embedded zeros.

The specifier `p` formats the pointer returned by [`lua_topointer`](#lua_topointer). That gives a unique string identifier for tables, userdata, threads, strings, and functions. For other values (numbers, nil, booleans), this specifier results in a string representing the pointer `NULL`.