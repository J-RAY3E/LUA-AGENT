# Variable Declarations

**Category**: Language

### 3.3.7 – Variable Declarations

Local and global variables can be declared anywhere inside a block. The declaration can include an initialization:

```lua
stat ::= local attnamelist [‘=’ explist]
stat ::= global attnamelist [‘=’ explist]
```

If there is no initialization, local variables are initialized with **nil**; global variables are left unchanged. Otherwise, the initialization gets the same adjustment of a multiple assignment (see [§3.3.3](#3.3.3)). Moreover, for global variables, the initialization will raise a runtime error if the variable is already defined, that is, it has a non-nil value.

The list of names may be prefixed by an attribute (a name between angle brackets) and each variable name may be postfixed by an attribute:

```lua
attnamelist ::=  [attrib] Name [attrib] {‘,’ Name [attrib]}
attrib ::= ‘<’ Name ‘>’
```

A prefixed attribute applies to all names in the list; a postfixed attribute applies to its particular name. There are two possible attributes: `const`, which declares a *constant* or *read-only* variable, that is, a variable that cannot be used as the left-hand side of an assignment, and `close`, which declares a to-be-closed variable (see [§3.3.8](#3.3.8)). Only local variables can have the `close` attribute. A list of variables can contain at most one to-be-closed variable.

Lua offers also a collective declaration for global variables:

```lua
stat ::= global [attrib] ‘*’
```

This special form implicitly declares as globals all names not explicitly declared previously. In particular, `global<const> *` implicitly declares as read-only globals all names not explicitly declared previously; see the following example:

```lua
global X
global<const> *
print(math.pi)   -- Ok, 'print' and 'math' are read-only
X = 1            -- Ok, declared as read-write
Y = 1            -- Error, Y is read-only
```

As noted in [§2.2](#2.2), all chunks start with an implicit declaration `global *`, but this preambular declaration becomes void inside the scope of any other **global** declaration. Therefore, a program that does not use global declarations or start with `global *` has free read-write access to any global; a program that starts with `global<const> *` has free read-only access to any global; and a program that starts with any other global declaration (e.g., `global none`) can only refer to declared variables.

Note that, for global variables, the effect of any declaration is only syntactical (except for the optional assignment):

```lua
global X <const>, _G
X = 1           -- ERROR
_ENV.X = 1      -- Ok
_G.print(X)     -- Ok
foo()         -- 'foo' can freely change any global
```

A chunk is also a block (see [§3.3.2](#3.3.2)), and so variables can be declared in a chunk outside any explicit block.

The visibility rules for variable declarations are explained in [§2.2](#2.2).