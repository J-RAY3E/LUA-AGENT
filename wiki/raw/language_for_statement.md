# For Statement

**Category**: Language

### 3.3.5 – For Statement

The **for** statement has two forms: one numerical and one generic.

#### The numerical **for** loop

The numerical **for** loop repeats a block of code while a control variable goes through an arithmetic progression. It has the following syntax:

```lua
stat ::= for Name ‘=’ exp ‘,’ exp [‘,’ exp] do block end
```

The given identifier (Name) defines the control variable, which is a new read-only (`const`) variable local to the loop body (*block*).

The loop starts by evaluating once the three control expressions. Their values are called respectively the *initial value*, the *limit*, and the *step*. If the step is absent, it defaults to 1.

If both the initial value and the step are integers, the loop is done with integers; note that the limit may not be an integer. Otherwise, the three values are converted to floats and the loop is done with floats. Beware of floating-point accuracy in this case.

After that initialization, the loop body is repeated with the value of the control variable going through an arithmetic progression, starting at the initial value, with a common difference given by the step. A negative step makes a decreasing sequence; a step equal to zero raises an error. The loop continues while the value is less than or equal to the limit (greater than or equal to for a negative step). If the initial value is already greater than the limit (or less than, if the step is negative), the body is not executed.

For integer loops, the control variable never wraps around; instead, the loop ends in case of an overflow.

#### The generic **for** loop

The generic **for** statement works over functions, called *iterators*. On each iteration, the iterator function is called to produce a new value, stopping when this new value is **nil**. The generic **for** loop has the following syntax:

```lua
stat ::= for namelist in explist do block end
namelist ::= Name {‘,’ Name}
```

A **for** statement like

```lua
for var_1, ···, var_n in explist do body end
```

works as follows.

The names *var\_i* declare loop variables local to the loop body. The first of these variables is the *control variable*, which is a read-only (`const`) variable.

The loop starts by evaluating *explist* to produce four values: an *iterator function*, a *state*, an initial value for the control variable, and a *closing value*.

Then, at each iteration, Lua calls the iterator function with two arguments: the state and the control variable. The results from this call are then assigned to the loop variables, following the rules of multiple assignments (see [§3.3.3](#3.3.3)). If the control variable becomes **nil**, the loop terminates. Otherwise, the body is executed and the loop goes to the next iteration.

The closing value behaves like a to-be-closed variable (see [§3.3.8](#3.3.8)), which can be used to release resources when the loop ends. Otherwise, it does not interfere with the loop.