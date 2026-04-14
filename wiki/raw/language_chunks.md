# Chunks

**Category**: Language

### 3.3.2 – Chunks

The unit of compilation of Lua is called a *chunk*. Syntactically, a chunk is simply a block:

```lua
chunk ::= block
```

Lua handles a chunk as the body of an anonymous function with a variable number of arguments (see [§3.4.11](#3.4.11)). As such, chunks can define local variables, receive arguments, and return values. Moreover, such anonymous function is compiled as in the scope of an external local variable called `_ENV` (see [§2.2](#2.2)). The resulting function always has `_ENV` as its only external variable, even if it does not use that variable.

A chunk can be stored in a file or in a string inside the host program. To execute a chunk, Lua first *loads* it, precompiling the chunk's code into instructions for a virtual machine, and then Lua executes the compiled code with an interpreter for the virtual machine.

Chunks can also be precompiled into binary form; see the program `luac` and the function [`string.dump`](#pdf-string.dump) for details. Programs in source and compiled forms are interchangeable; Lua automatically detects the file type and acts accordingly (see [`load`](#pdf-load)). Be aware that, unlike source code, maliciously crafted binary chunks can crash the interpreter.