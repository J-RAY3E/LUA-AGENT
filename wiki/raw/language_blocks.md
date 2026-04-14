# Blocks

**Category**: Language

### 3.3.1 – Blocks

A block is a list of statements, which are executed sequentially:

```lua
block ::= {stat}
```

Lua has *empty statements* that allow you to separate statements with semicolons, start a block with a semicolon or write two semicolons in sequence:

```lua
stat ::= ‘;’
```

Both function calls and assignments can start with an open parenthesis. This possibility leads to an ambiguity in Lua's grammar. Consider the following fragment:

```lua
a = b + c
(print or io.write)('done')
```

The grammar could see this fragment in two ways:

```lua
a = b + c(print or io.write)('done')

a = b + c; (print or io.write)('done')
```

The current parser always sees such constructions in the first way, interpreting the open parenthesis as the start of the arguments to a call. To avoid this ambiguity, it is a good practice to always precede with a semicolon statements that start with a parenthesis:

```lua
;(print or io.write)('done')
```

A block can be explicitly delimited to produce a single statement:

```lua
stat ::= do block end
```

Explicit blocks are useful to control the scope of variable declarations. Explicit blocks are also sometimes used to add a **return** statement in the middle of another block (see [§3.3.4](#3.3.4)).