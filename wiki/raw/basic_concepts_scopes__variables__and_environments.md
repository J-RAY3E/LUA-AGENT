# Scopes, Variables, and Environments

**Category**: Basic Concepts

## 2.2 – Scopes, Variables, and Environments

A variable name refers to a global or a local variable according to the declaration that is in context at that point of the code. (For the purposes of this discussion, a function's formal parameter is equivalent to a local variable.)

All chunks start with an implicit declaration `global *`, which declares all free names as global variables; this preambular declaration becomes void inside the scope of any other **global** declaration, as the following example illustrates:

```lua
X = 1       -- Ok, global by default
do
  global Y  -- voids the implicit initial declaration
  Y = 1     -- Ok, Y declared as global
  X = 1     -- ERROR, X not declared
end
X = 2       -- Ok, global by default again
```

So, outside any global declaration, Lua works as global-by-default. Inside any global declaration, Lua works without a default: All variables must be declared.

Lua is a lexically scoped language. The scope of a variable declaration begins at the first statement after the declaration and lasts until the last non-void statement of the innermost block that includes the declaration. (*Void statements* are labels and empty statements.)

A declaration shadows any declaration for the same name that is in context at the point of the declaration. Inside this shadow, any outer declaration for that name is void. See the next example:

```lua
global print, x
x = 10                -- global variable
do                    -- new block
  local x = x         -- new 'x', with value 10
  print(x)            --> 10
  x = x+1
  do                  -- another block
    local x = x+1     -- another 'x'
    print(x)          --> 12
  end
  print(x)            --> 11
end
print(x)              --> 10  (the global one)
```

Notice that, in a declaration like `local x = x`, the new `x` being declared is not in scope yet, and so the `x` on the right-hand side refers to the outside variable.

Because of the lexical scoping rules, local variables can be freely accessed by functions defined inside their scope. A local variable used by an inner function is called an *upvalue* (or *external local variable*, or simply *external variable*) inside the inner function.

Notice that each execution of a **local** statement defines new local variables. Consider the following example:

```lua
a = {}
local x = 20
for i = 1, 10 do
  local y = 0
  a[i] = function () y = y + 1; return x + y end
end
```

The loop creates ten closures (that is, ten instances of the anonymous function). Each of these closures uses a different `y` variable, while all of them share the same `x`.

As we will discuss further in [§3.2](#3.2) and [§3.3.3](#3.3.3), any reference to a global variable `var` is syntactically translated to `_ENV.var`. Moreover, every chunk is compiled in the scope of an external local variable named `_ENV` (see [§3.3.2](#3.3.2)), so `_ENV` itself is never a free name in a chunk.

Despite the existence of this external `_ENV` variable and the translation of free names, `_ENV` is a regular name. In particular, you can define new variables and parameters with that name. (However, you should not define `_ENV` as a global variable, otherwise `_ENV.var` would translate to `_ENV._ENV.var` and so on, in an infinite loop.) Each reference to a global variable name uses the `_ENV` that is visible at that point in the program.

Any table used as the value of `_ENV` is called an *environment*.

Lua keeps a distinguished environment called the *global environment*. This value is kept at a special index in the C registry (see [§4.3](#4.3)). In Lua, the global variable [`_G`](#pdf-_G) is initialized with this same value. ([`_G`](#pdf-_G) is never used internally, so changing its value will affect only your own code.)

When Lua loads a chunk, the default value for its `_ENV` variable is the global environment (see [`load`](#pdf-load)). Therefore, by default, global variables in Lua code refer to entries in the global environment and, therefore, they act as conventional global variables. Moreover, all standard libraries are loaded in the global environment and some functions there operate on that environment. You can use [`load`](#pdf-load) (or [`loadfile`](#pdf-loadfile)) to load a chunk with a different environment. (In C, you have to load the chunk and then change the value of its first upvalue; see [`lua_setupvalue`](#lua_setupvalue).)