# math.frexp()

**Category**: Standard Libraries

### `math.frexp (x)`

Returns two numbers `m` and `e` such that *x = m2e*, where `e` is an integer. When `x` is zero, NaN, +inf, or -inf, `m` is equal to `x`; otherwise, the absolute value of `m` is in the range *[0.5, 1)* .