# Expressions

**Category**: Language

## 3.4 – Expressions

The basic expressions in Lua are the following:

```lua
exp ::= prefixexp
exp ::= nil | false | true
exp ::= Numeral
exp ::= LiteralString
exp ::= functiondef
exp ::= tableconstructor
exp ::= ‘...’
exp ::= exp binop exp
exp ::= unop exp
prefixexp ::= var | functioncall | ‘(’ exp ‘)’
```

Numerals and literal strings are explained in [§3.1](#3.1); variables are explained in [§3.2](#3.2); function definitions are explained in [§3.4.11](#3.4.11); function calls are explained in [§3.4.10](#3.4.10); table constructors are explained in [§3.4.9](#3.4.9). Vararg expressions, denoted by three dots ('`...`'), can only be used when directly inside a variadic function; they are explained in [§3.4.11](#3.4.11).

Binary operators comprise arithmetic operators (see [§3.4.1](#3.4.1)), bitwise operators (see [§3.4.2](#3.4.2)), relational operators (see [§3.4.4](#3.4.4)), logical operators (see [§3.4.5](#3.4.5)), and the concatenation operator (see [§3.4.6](#3.4.6)). Unary operators comprise the unary minus (see [§3.4.1](#3.4.1)), the unary bitwise NOT (see [§3.4.2](#3.4.2)), the unary logical **not** (see [§3.4.5](#3.4.5)), and the unary *length operator* (see [§3.4.7](#3.4.7)).