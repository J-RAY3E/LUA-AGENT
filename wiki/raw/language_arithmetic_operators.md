# Arithmetic Operators

**Category**: Language

### 3.4.1 – Arithmetic Operators

Lua supports the following arithmetic operators:

* `+`: addition
* `-`: subtraction
* `*`: multiplication
* `/`: float division
* `//`: floor division
* `%`: modulo
* `^`: exponentiation
* `-`: unary minus

With the exception of exponentiation and float division, the arithmetic operators work as follows: If both operands are integers, the operation is performed over integers and the result is an integer. Otherwise, if both operands are numbers, then they are converted to floats, the operation is performed following the machine's rules for floating-point arithmetic (usually the IEEE 754 standard), and the result is a float. (The string library coerces strings to numbers in arithmetic operations; see [§3.4.3](#3.4.3) for details.)

Exponentiation and float division (`/`) always convert their operands to floats and the result is always a float. Exponentiation uses the ISO C function `pow`, so that it works for non-integer exponents too.

Floor division (`//`) is a division that rounds the quotient towards minus infinity, resulting in the floor of the division of its operands.

Modulo is defined as the remainder of a division that rounds the quotient towards minus infinity (floor division).

In case of overflows in integer arithmetic, all operations *wrap around*.