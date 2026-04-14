# Bitwise Operators

**Category**: Language

### 3.4.2 – Bitwise Operators

Lua supports the following bitwise operators:

* `&`: bitwise AND
* `|`: bitwise OR
* `~`: bitwise exclusive OR
* `>>`: right shift
* `<<`: left shift
* `~`: unary bitwise NOT

All bitwise operations convert its operands to integers (see [§3.4.3](#3.4.3)), operate on all bits of those integers, and result in an integer.

Both right and left shifts fill the vacant bits with zeros. Negative displacements shift to the other direction; displacements with absolute values equal to or higher than the number of bits in an integer result in zero (as all bits are shifted out).