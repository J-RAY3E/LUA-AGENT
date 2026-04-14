# lua_getinfo

**Category**: API

### `lua_getinfo`[-(0|1), +(0|1|2), *m*]

```lua
int lua_getinfo (lua_State *L, const char *what, lua_Debug *ar);
```

Gets information about a specific function or function invocation.

To get information about a function invocation, the parameter `ar` must be a valid activation record that was filled by a previous call to [`lua_getstack`](#lua_getstack) or given as argument to a hook (see [`lua_Hook`](#lua_Hook)).

To get information about a function, you push it onto the stack and start the `what` string with the character '`>`'. (In that case, `lua_getinfo` pops the function from the top of the stack.) For instance, to know in which line a function `f` was defined, you can write the following code:

```lua
lua_Debug ar;
lua_getglobal(L, "f");  /* get global 'f' */
lua_getinfo(L, ">S", &ar);
printf("%d\n", ar.linedefined);
```

Each character in the string `what` selects some fields of the structure `ar` to be filled or a value to be pushed on the stack. (These characters are also documented in the declaration of the structure [`lua_Debug`](#lua_Debug), between parentheses in the comments following each field.)

* '`f`': pushes onto the stack the function that is running at the given level;
* '`l`': fills in the field `currentline`;
* '`n`': fills in the fields `name` and `namewhat`;
* '`r`': fills in the fields `ftransfer` and `ntransfer`;
* '`S`': fills in the fields `source`, `short_src`, `linedefined`, `lastlinedefined`, and `what`;
* '`t`': fills in the fields `istailcall` and `extraargs`;
* '`u`': fills in the fields `nups`, `nparams`, and `isvararg`;
* '`L`': pushes onto the stack a table whose indices are the lines on the function with some associated code, that is, the lines where you can put a break point. (Lines with no code include empty lines and comments.) If this option is given together with option '`f`', its table is pushed after the function. This is the only option that can raise a memory error.

This function returns 0 to signal an invalid option in `what`; even then the valid options are handled correctly.