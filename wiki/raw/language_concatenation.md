# Concatenation

**Category**: Language

### 3.4.6 – Concatenation

The string concatenation operator in Lua is denoted by two dots ('`..`'). If both operands are strings or numbers, then the numbers are converted to strings in a non-specified format (see [§3.4.3](#3.4.3)). Otherwise, the `__concat` metamethod is called (see [§2.4](#2.4)).