# math.randomseed()

**Category**: Standard Libraries

### `math.randomseed ([x [, y]])`

When called with at least one argument, the integer parameters `x` and `y` are joined into a *seed* that is used to reinitialize the pseudo-random generator; equal seeds produce equal sequences of numbers. The default for `y` is zero.

When called with no arguments, Lua generates a seed with a weak attempt for randomness.

This function returns the two seed components that were effectively used, so that setting them again repeats the sequence.

To ensure a required level of randomness to the initial state (or contrarily, to have a deterministic sequence, for instance when debugging a program), you should call [`math.randomseed`](#pdf-math.randomseed) with explicit arguments.