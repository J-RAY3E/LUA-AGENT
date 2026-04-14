# Function Definitions

**Category**: Language

### 3.4.11 – Function Definitions

The syntax for a function definition is

```lua
functiondef ::= function funcbody
funcbody ::= ‘(’ [parlist] ‘)’ block end
```

The following syntactic sugar simplifies function definitions:

```lua
stat ::= function funcname funcbody
stat ::= local function Name funcbody
stat ::= global function Name funcbody
funcname ::= Name {‘.’ Name} [‘:’ Name]
```

The statement

```lua
function f () body end
```

translates to

```lua
f = function () body end
```

The statement

```lua
function t.a.b.c.f () body end
```

translates to

```lua
t.a.b.c.f = function () body end
```

The statement

```lua
local function f () body end
```

translates to

```lua
local f; f = function () body end
```

not to

```lua
local f = function () body end
```

(This only makes a difference when the body of the function contains recursive references to `f`.) Similarly, the statement

```lua
global function f () body end
```

translates to

```lua
global f; global f = function () body end
```

The second **global** makes the assignment an initialization, which will raise an error if that global is already defined.

The *colon* syntax is used to emulate *methods*, adding an implicit extra parameter `self` to the function. Thus, the statement

```lua
function t.a.b.c:f (params) body end
```

is syntactic sugar for

```lua
t.a.b.c.f = function (self, params) body end
```

A function definition is an executable expression, whose value has type *function*. When Lua precompiles a chunk, all its function bodies are precompiled too, but they are not created yet. Then, whenever Lua executes the function definition, the function is *instantiated* (or *closed*). This function instance, or *closure*, is the final value of the expression.

Results are returned using the **return** statement (see [§3.3.4](#3.3.4)). If control reaches the end of a function without encountering a **return** statement, then the function returns with no results.

There is a system-dependent limit on the number of values that a function may return. This limit is guaranteed to be at least 1000.

#### Parameters

Parameters act as local variables that are initialized with the argument values:

```lua
parlist ::= namelist [‘,’ varargparam] | varargparam
varargparam ::= ‘...’ [Name]
```

When a Lua function is called, it adjusts its list of arguments to the length of its list of parameters (see [§3.4.12](#3.4.12)), unless the function is a *variadic function*, which is indicated by three dots ('`...`') at the end of its parameter list. A variadic function does not adjust its argument list; instead, it collects all extra arguments and supplies them to the function through a *vararg table*. In that table, the values at indices 1, 2, etc. are the extra arguments, and the value at index "`n`" is the number of extra arguments.

As an example, consider the following definitions:

```lua
function f(a, b) end
function g(a, b, ...) end
function r() return 1,2,3 end
```

Then, we have the following mapping from arguments to parameters and to the vararg table:

```lua
CALL             PARAMETERS

f(3)             a=3, b=nil
f(3, 4)          a=3, b=4
f(3, 4, 5)       a=3, b=4
f(r(), 10)       a=1, b=10
f(r())           a=1, b=2

g(3)             a=3, b=nil, va. table ->  {n = 0}
g(3, 4)          a=3, b=4,   va. table ->  {n = 0}
g(3, 4, 5, 8)    a=3, b=4,   va. table ->  {5, 8, n = 2}
g(5, r())        a=5, b=1,   va. table ->  {2, 3, n = 2}
```

A vararg table in a variadic function can have an optional name, given after the three dots. When present, that name denotes a read-only local variable that refers to the vararg table. If the vararg table does not have a name, it can only be accessed through a vararg expression.

A vararg expression is also written as three dots, and its value is a list of the values in the vararg table, from 1 to the integer value at index "`n`". (Therefore, if the code does not modify the vararg table, this list corresponds to the extra arguments in the function call.) This list behaves like the results from a function with multiple results (see [§3.4.12](#3.4.12)).

As an optimization, if the vararg table satisfies some conditions, the code does not create an actual table and instead translates the indexing expressions and the vararg expressions into accesses to the internal vararg data. The conditions are as follows: If the vararg table has a name, that name is not an upvalue in a nested function and it is used only as the base table in the syntactic constructions `t[exp]` or `t.id`. Note that an anonymous vararg table always satisfy these conditions.