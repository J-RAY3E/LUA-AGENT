# 7 – Lua Standalone

**Category**: Manual

# 7 – Lua Standalone

Although Lua has been designed as an extension language, to be embedded in a host C program, it is also frequently used as a standalone language. An interpreter for Lua as a standalone language, called simply `lua`, is provided with the standard distribution. The standalone interpreter includes all standard libraries. Its usage is:

```lua
lua [options] [script [args]]
```

The options are:

* `-e stat`: execute string *stat*;
* `-i`: enter interactive mode after running *script*;
* `-l mod`: "require" *mod* and assign the result to global *mod*;
* `-l g=mod`: "require" *mod* and assign the result to global *g*;
* `-v`: print version information;
* `-E`: ignore environment variables;
* `-W`: turn warnings on;
* `--`: stop handling options;
* `-`: execute `stdin` as a file and stop handling options.

After handling its options, `lua` runs the given *script*. When called without arguments, `lua` behaves as `lua -v -i` when the standard input (`stdin`) is a terminal, and as `lua -` otherwise.

When called without the option `-E`, the interpreter checks for an environment variable `LUA_INIT_5_5` (or `LUA_INIT` if the versioned name is not defined) before running any argument. If the variable content has the format `@filename`, then `lua` executes the file. Otherwise, `lua` executes the string itself.

When called with the option `-E`, Lua does not consult any environment variables. In particular, the values of [`package.path`](#pdf-package.path) and [`package.cpath`](#pdf-package.cpath) are set with the default paths defined in `luaconf.h`. To signal to the libraries that this option is on, the stand-alone interpreter sets the field `"LUA_NOENV"` in the registry to a true value. Other libraries may consult this field for the same purpose.

The options `-e`, `-l`, and `-W` are handled in the order they appear. For instance, an invocation like

```lua
$ lua -e 'a=1' -llib1 script.lua
```

will first set `a` to 1, then require the library `lib1`, and finally run the file `script.lua` with no arguments. (Here `$` is the shell prompt. Your prompt may be different.)

Before running any code, `lua` collects all command-line arguments in a global table called `arg`. The script name goes to index 0, the first argument after the script name goes to index 1, and so on. Any arguments before the script name (that is, the interpreter name plus its options) go to negative indices. For instance, in the call

```lua
$ lua -la b.lua t1 t2
```

the table is like this:

```lua
arg = { [-2] = "lua", [-1] = "-la",
        [0] = "b.lua",
        [1] = "t1", [2] = "t2" }
```

If there is no script in the call, the interpreter name goes to index 0, followed by the other arguments. For instance, the call

```lua
$ lua -e "print(arg[1])"
```

will print "`-e`". If there is a script, the script is called with arguments `arg[1]`, ···, `arg[#arg]`. Like all chunks in Lua, the script is compiled as a variadic function.

In interactive mode, Lua repeatedly prompts and waits for a line. After reading a line, Lua first tries to interpret the line as an expression. If it succeeds, it prints its value. Otherwise, it interprets the line as a chunk. If you write an incomplete chunk, the interpreter waits for its completion by issuing a different prompt.

Note that, as each complete line is read as a new chunk, local variables do not outlive lines. To steer clear of confusion, the interpreter gives a warning if a line starts with the reserved word **local**:

```lua
> x = 20      -- global 'x'
> local x = 10; print(x)
    --> warning: locals do not survive across lines in interactive mode
    --> 10
> print(x)     -- back to global 'x'
    --> 20
> do       -- incomplete chunk
>> local x = 10; print(x)    -- '>>' prompts for line completion
>> print(x)
>> end     -- chunk completed
   --> 10
   --> 10
```

If the global variable `_PROMPT` contains a string, then its value is used as the prompt. Similarly, if the global variable `_PROMPT2` contains a string, its value is used as the secondary prompt (issued during incomplete statements).

In case of unprotected errors in the script, the interpreter reports the error to the standard error stream. If the error object is not a string but has a metamethod `__tostring`, the interpreter calls this metamethod to produce the final message. Otherwise, the interpreter converts the error object to a string and adds a stack traceback to it. When warnings are on, they are simply printed in the standard error output.

When finishing normally, the interpreter closes its main Lua state (see [`lua_close`](#lua_close)). The script can avoid this step by calling [`os.exit`](#pdf-os.exit) to terminate.

To allow the use of Lua as a script interpreter in Unix systems, Lua skips the first line of a file chunk if it starts with `#`. Therefore, Lua scripts can be made into executable programs by using `chmod +x` and the `#!` form, as in

```lua
#!/usr/local/bin/lua
```

Of course, the location of the Lua interpreter may be different in your machine. If `lua` is in your `PATH`, then

```lua
#!/usr/bin/env lua
```

is a more portable solution.