# Variables

**Category**: Language

## 3.2 – Variables

Variables are places that store values. There are three kinds of variables in Lua: global variables, local variables, and table fields.

A single name can denote a global variable or a local variable (or a function's formal parameter, which is a particular kind of local variable) (see [§2.2](#2.2)):

```lua
var ::= Name
```

Name denotes identifiers (see [§3.1](#3.1)).

Because variables are *lexically scoped*, local variables can be freely accessed by functions defined inside their scope (see [§2.2](#2.2)).

Before the first assignment to a variable, its value is **nil**.

Square brackets are used to index a table:

```lua
var ::= prefixexp ‘[’ exp ‘]’
```

The meaning of accesses to table fields can be changed via metatables (see [§2.4](#2.4)).

The syntax `var.Name` is just syntactic sugar for `var["Name"]`:

```lua
var ::= prefixexp ‘.’ Name
```

An access to a global variable `x` is equivalent to `_ENV.x`.