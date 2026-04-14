# Control Structures

**Category**: Language

### 3.3.4 – Control Structures

The control structures **if**, **while**, and **repeat** have the usual meaning and familiar syntax:

```lua
stat ::= while exp do block end
stat ::= repeat block until exp
stat ::= if exp then block {elseif exp then block} [else block] end
```

Lua also has a **for** statement, in two flavors (see [§3.3.5](#3.3.5)).

The condition expression of a control structure can return any value. Both **false** and **nil** test false. All values different from **nil** and **false** test true. In particular, the number 0 and the empty string also test true.

In the **repeat**–**until** loop, the inner block does not end at the **until** keyword, but only after the condition. So, the condition can refer to local variables declared inside the loop block.

The **goto** statement transfers the program control to a label. For syntactical reasons, labels in Lua are considered statements too:

```lua
stat ::= goto Name
stat ::= label
label ::= ‘::’ Name ‘::’
```

A label is visible in the entire block where it is defined, except inside nested functions. A goto can jump to any visible label as long as it does not enter into the scope of a variable declaration. A label should not be declared where a previous label with the same name is visible, even if this other label has been declared in an enclosing block.

The **break** statement terminates the execution of a **while**, **repeat**, or **for** loop, skipping to the next statement after the loop:

```lua
stat ::= break
```

A **break** ends the innermost enclosing loop.

The **return** statement is used to return values from a function or a chunk (which is handled as an anonymous function). Functions can return more than one value, so the syntax for the **return** statement is

```lua
stat ::= return [explist] [‘;’]
```

The **return** statement can only be written as the last statement of a block. If it is necessary to **return** in the middle of a block, then an explicit inner block can be used, as in the idiom `do return end`, because now **return** is the last statement in its (inner) block.