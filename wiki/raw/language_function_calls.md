# Function Calls

**Category**: Language

### 3.4.10 – Function Calls

A function call in Lua has the following syntax:

```lua
functioncall ::= prefixexp args
```

In a function call, first prefixexp and args are evaluated. If the value of prefixexp has type *function*, then this function is called with the given arguments. Otherwise, if present, the prefixexp `__call` metamethod is called: its first argument is the value of prefixexp, followed by the original call arguments (see [§2.4](#2.4)).

The form

```lua
functioncall ::= prefixexp ‘:’ Name args
```

can be used to emulate methods. A call `v:name(args)` is syntactic sugar for `v.name(v, args)`, except that `v` is evaluated only once.

Arguments have the following syntax:

```lua
args ::= ‘(’ [explist] ‘)’
args ::= tableconstructor
args ::= LiteralString
```

All argument expressions are evaluated before the call. A call of the form `f{fields}` is syntactic sugar for `f({fields})`; that is, the argument list is a single new table. A call of the form `f'string'` (or `f"string"` or `f[[string]]`) is syntactic sugar for `f('string')`; that is, the argument list is a single literal string.

A call of the form `return functioncall` not in the scope of a to-be-closed variable is called a *tail call*. Lua implements *proper tail calls* (or *proper tail recursion*): In a tail call, the called function reuses the stack entry of the calling function. Therefore, there is no limit on the number of nested tail calls that a program can execute. However, a tail call erases any debug information about the calling function. Note that a tail call only happens with a particular syntax, where the **return** has one single function call as argument, and it is outside the scope of any to-be-closed variable. This syntax makes the calling function return exactly the returns of the called function, without any intervening action. So, none of the following examples are tail calls:

```lua
return (f(x))        -- results adjusted to 1
return 2 * f(x)      -- result multiplied by 2
return x, f(x)       -- additional results
f(x); return         -- results discarded
return x or f(x)     -- results adjusted to 1
```