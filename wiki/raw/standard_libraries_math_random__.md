# math.random()

**Category**: Standard Libraries

### `math.random ([m [, n]])`

When called without arguments, returns a pseudo-random float with uniform distribution in the range *[0, 1)*. When called with two integers `m` and `n`, `math.random` returns a pseudo-random integer with uniform distribution in the range *[m, n]*. The call `math.random(n)`, for a positive `n`, is equivalent to `math.random(1,n)`. The call `math.random(0)` produces an integer with all bits (pseudo)random.

This function uses the `xoshiro256**` algorithm to produce pseudo-random 64-bit integers, which are the results of calls with argument 0. Other results (ranges and floats) are unbiased extracted from these integers.

Lua initializes its pseudo-random generator with the equivalent of a call to [`math.randomseed`](#pdf-math.randomseed) with no arguments, so that `math.random` should generate different sequences of results each time the program runs.