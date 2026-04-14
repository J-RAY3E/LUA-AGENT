# 8 – Incompatibilities with the Previous Version

**Category**: Manual

# 8 – Incompatibilities with the Previous Version

Here we list the incompatibilities that you may find when moving a program from Lua 5.4 to Lua 5.5.

You can avoid some incompatibilities by compiling Lua with appropriate options (see file `luaconf.h`). However, all these compatibility options will be removed in the future. More often than not, compatibility issues arise when these compatibility options are removed. So, whenever you have the chance, you should try to test your code with a version of Lua compiled with all compatibility options turned off. That will ease transitions to newer versions of Lua.

Lua versions can always change the C API in ways that do not imply source-code changes in a program, such as the numeric values for constants or the implementation of functions as macros. Therefore, you should never assume that binaries are compatible between different Lua versions. Always recompile clients of the Lua API when using a new version.

Similarly, Lua versions can always change the internal representation of precompiled chunks; precompiled chunks are not compatible between different Lua versions.

The standard paths in the official distribution may change between versions.

## 8.1 – Incompatibilities in the Language

* The word **global** is a reserved word. Do not use it as a regular name.
* The control variable in **for** loops is read only. If you need to change it, declare a local variable with the same name in the loop body.
* A chain of `__call` metamethods can have at most 15 objects.
* In an error, a **nil** as the error object is replaced by a string message.

## 8.2 – Incompatibilities in the Libraries

* Parameters for the garbage collection are not set with the options "`incremental`" and "`generational`"; instead, there is a new option "`param`" to that end. Moreover, there were some changes in the parameters themselves.

## 8.3 – Incompatibilities in the API

* In [`lua_call`](#lua_call) and related functions, the maximum value for the number of required results (`nresults`) is 250. If you really need a larger value, use [`LUA_MULTRET`](#pdf-LUA_MULTRET) and then adjust the stack size. Previously, this limit was unspecified.
* [`lua_newstate`](#lua_newstate) has a third parameter, a seed for the hashing of strings.
* The function `lua_resetthread` is deprecated; it is equivalent to [`lua_closethread`](#lua_closethread) with `from` being `NULL`.
* The function `lua_setcstacklimit` is deprecated. Calls to it can simply be removed.
* The function [`lua_dump`](#lua_dump) changed the way it keeps the stack through the calls to the writer function. (That was not specified in previous versions.) Also, it calls the writer function one extra time, to signal the end of the dump.
* Parameters for the garbage collection are not set with the options [`LUA_GCINC`](#pdf-LUA_GCINC) and [`LUA_GCGEN`](#pdf-LUA_GCGEN); instead, there is a new option [`LUA_GCPARAM`](#pdf-LUA_GCPARAM) to that end. Moreover, there were some changes in the parameters themselves.
* The function [`lua_pushvfstring`](#lua_pushvfstring) now reports errors, instead of raising them.