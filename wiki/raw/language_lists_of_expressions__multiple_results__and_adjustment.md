# Lists of Expressions, Multiple Results, and Adjustment

**Category**: Language

### 3.4.12 – Lists of Expressions, Multiple Results, and Adjustment

Both function calls and vararg expressions can result in multiple values. These expressions are called *multires expressions*.

When a multires expression is used as the last element of a list of expressions, all results from the expression are added to the list of values produced by the list of expressions. Note that a single expression in a place that expects a list of expressions is the last expression in that (singleton) list.

These are the places where Lua expects a list of expressions:

* A **return** statement, for instance `return e1,e2,e3` (see [§3.3.4](#3.3.4)).
* A table constructor, for instance `{e1,e2,e3}` (see [§3.4.9](#3.4.9)).
* The arguments of a function call, for instance `foo(e1,e2,e3)` (see [§3.4.10](#3.4.10)).
* A multiple assignment, for instance `a,b,c = e1,e2,e3` (see [§3.3.3](#3.3.3)).
* A local or global declaration, which is similar to a multiple assignment.
* The initial values in a generic **for** loop, for instance `for k in e1,e2,e3 do ... end` (see [§3.3.5](#3.3.5)).

In the last four cases, the list of values from the list of expressions must be *adjusted* to a specific length: the number of parameters in a call to a non-variadic function (see [§3.4.11](#3.4.11)), the number of variables in a multiple assignment or a declaration, and exactly four values for a generic **for** loop. The *adjustment* follows these rules: If there are more values than needed, the extra values are thrown away; if there are fewer values than needed, the list is extended with **nil**'s. When the list of expressions ends with a multires expression, all results from that expression enter the list of values before the adjustment.

When a multires expression is used in a list of expressions without being the last element, or in a place where the syntax expects a single expression, Lua adjusts the result list of that expression to one element. As a particular case, the syntax expects a single expression inside a parenthesized expression; therefore, adding parentheses around a multires expression forces it to produce exactly one result.

We seldom need to use a vararg expression in a place where the syntax expects a single expression. (Usually it is simpler to add a regular parameter before the variadic part and use that parameter.) When there is such a need, we recommend assigning the vararg expression to a single variable and using that variable in its place.

Here are some examples of uses of multires expressions. In all cases, when the construction needs "the n-th result" and there is no such result, it uses a **nil**.

```lua
print(x, f())      -- prints x and all results from f().
print(x, (f()))    -- prints x and the first result from f().
print(f(), x)      -- prints the first result from f() and x.
print(1 + f())     -- prints 1 added to the first result from f().
local x = ...      -- x gets the first vararg argument.
x,y = ...          -- x gets the first vararg argument,
                   -- y gets the second vararg argument.
x,y,z = w, f()     -- x gets w, y gets the first result from f(),
                   -- z gets the second result from f().
x,y,z = f()        -- x gets the first result from f(),
                   -- y gets the second result from f(),
                   -- z gets the third result from f().
x,y,z = f(), g()   -- x gets the first result from f(),
                   -- y gets the first result from g(),
                   -- z gets the second result from g().
x,y,z = (f())      -- x gets the first result from f(), y and z get nil.
return f()         -- returns all results from f().
return x, ...      -- returns x and all received vararg arguments.
return x,y,f()     -- returns x, y, and all results from f().
{f()}              -- creates a list with all results from f().
{...}              -- creates a list with all vararg arguments.
{f(), 5}           -- creates a list with the first result from f() and 5.
```