# table.move()

**Category**: Standard Libraries

### `table.move (a1, f, e, t [,a2])`

Moves elements from the table `a1` to the table `a2`, performing the equivalent to the following multiple assignment: `a2[t],··· = a1[f],···,a1[e]`. The default for `a2` is `a1`. The destination range can overlap with the source range. The number of elements to be moved must fit in a Lua integer. If `f` is larger than `e`, nothing is moved.

Returns the destination table `a2`.