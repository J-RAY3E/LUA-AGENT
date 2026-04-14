# Assignment

**Category**: Language

### 3.3.3 – Assignment

Lua allows multiple assignments. Therefore, the syntax for assignment defines a list of variables on the left side and a list of expressions on the right side. The elements in both lists are separated by commas:

```lua
stat ::= varlist ‘=’ explist
varlist ::= var {‘,’ var}
explist ::= exp {‘,’ exp}
```

Expressions are discussed in [§3.4](#3.4).

Before the assignment, the list of values is *adjusted* to the length of the list of variables (see [§3.4.12](#3.4.12)).

If a variable is both assigned and read inside a multiple assignment, Lua ensures that all reads get the value of the variable before the assignment. Thus the code

```lua
i = 3
i, a[i] = i+1, 20
```

sets `a[3]` to 20, without affecting `a[4]` because the `i` in `a[i]` is evaluated (to 3) before it is assigned 4. Similarly, the line

```lua
x, y = y, x
```

exchanges the values of `x` and `y`, and

```lua
x, y, z = y, z, x
```

cyclically permutes the values of `x`, `y`, and `z`.

Note that this guarantee covers only accesses syntactically inside the assignment statement. If a function or a metamethod called during the assignment changes the value of a variable, Lua gives no guarantees about the order of that access.

An assignment to a global name `x = val` is equivalent to the assignment `_ENV.x = val` (see [§2.2](#2.2)).

The meaning of assignments to table fields and global variables (which are actually table fields, too) can be changed via metatables (see [§2.4](#2.4)).