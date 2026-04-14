# Relational Operators

**Category**: Language

### 3.4.4 – Relational Operators

Lua supports the following relational operators:

* `==`: equality
* `~=`: inequality
* `<`: less than
* `>`: greater than
* `<=`: less or equal
* `>=`: greater or equal

These operators always result in **false** or **true**.

Equality (`==`) first compares the type of its operands. If the types are different, then the result is **false**. Otherwise, the values of the operands are compared. Strings are equal if they have the same byte content. Numbers are equal if they denote the same mathematical value.

Tables, userdata, and threads are compared by reference: two objects are considered equal only if they are the same object. Every time you create a new object (a table, a userdata, or a thread), this new object is different from any previously existing object. A function is always equal to itself. Functions with any detectable difference (different behavior, different definition) are always different. Functions created at different times but with no detectable differences may be classified as equal or not (depending on internal caching details).

You can change the way that Lua compares tables and userdata by using the `__eq` metamethod (see [§2.4](#2.4)).

Equality comparisons do not convert strings to numbers or vice versa. Thus, `"0"==0` evaluates to **false**, and `t[0]` and `t["0"]` denote different entries in a table.

The operator `~=` is exactly the negation of equality (`==`).

The order operators work as follows. If both arguments are numbers, then they are compared according to their mathematical values, regardless of their subtypes. Otherwise, if both arguments are strings, then their values are compared according to the current locale. Otherwise, Lua tries to call the `__lt` or the `__le` metamethod (see [§2.4](#2.4)). A comparison `a > b` is translated to `b < a` and `a >= b` is translated to `b <= a`.

Following the IEEE 754 standard, the special value NaN is considered neither less than, nor equal to, nor greater than any value, including itself.