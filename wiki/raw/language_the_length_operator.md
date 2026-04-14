# The Length Operator

**Category**: Language

### 3.4.7 – The Length Operator

The length operator is denoted by the unary prefix operator `#`.

The length of a string is its number of bytes. (That is the usual meaning of string length when each character is one byte.)

The length operator applied on a table returns a border in that table. A *border* in a table `t` is any non-negative integer that satisfies the following condition:

```lua
(border == 0 or t[border] ~= nil) and
(t[border + 1] == nil or border == math.maxinteger)
```

In words, a border is any positive integer index present in the table that is followed by an absent index, plus two limit cases: zero, when index 1 is absent; and the maximum value for an integer, when that index is present. Note that keys that are not positive integers do not interfere with borders.

A table with exactly one border is called a *sequence*. For instance, the table `{10,20,30,40,50}` is a sequence, as it has only one border (5). The table `{10,20,30,nil,50}` has two borders (3 and 5), and therefore it is not a sequence. (The **nil** at index 4 is called a *hole*.) The table `{nil,20,30,nil,nil,60,nil}` has three borders (0, 3, and 6), so it is not a sequence, too. The table `{}` is a sequence with border 0.

When `t` is a sequence, `#t` returns its only border, which corresponds to the intuitive notion of the length of the sequence. When `t` is not a sequence, `#t` can return any of its borders. (The exact one depends on details of the internal representation of the table, which in turn can depend on how the table was populated and the memory addresses of its non-numeric keys.)

The computation of the length of a table has a guaranteed worst time of *O(log n)*, where *n* is the largest integer key in the table.

A program can modify the behavior of the length operator for any value but strings through the `__len` metamethod (see [§2.4](#2.4)).