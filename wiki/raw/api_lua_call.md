# lua_call

**Category**: API

### `lua_call`[-(nargs+1), +nresults, *e*]

```lua
void lua_call (lua_State *L, int nargs, int nresults);
```

Calls a function. Like regular Lua calls, `lua_call` respects the `__call` metamethod. So, here the word "function" means any callable value.

To do a call you must use the following protocol: first, the function to be called is pushed onto the stack; then, the arguments to the call are pushed in direct order; that is, the first argument is pushed first. Finally you call [`lua_call`](#lua_call); `nargs` is the number of arguments that you pushed onto the stack. When the function returns, all arguments and the function value are popped and the call results are pushed onto the stack. The number of results is adjusted to `nresults`, unless `nresults` is `LUA_MULTRET`, which makes all results from the function to be pushed. In the first case, an explicit number of results, the caller must ensure that the stack has space for the returned values. In the second case, all results, Lua takes care that the returned values fit into the stack space, but it does not ensure any extra space in the stack. The function results are pushed onto the stack in direct order (the first result is pushed first), so that after the call the last result is on the top of the stack.

The maximum value for `nresults` is 250.

Any error while calling and running the function is propagated upwards (with a `longjmp`).

The following example shows how the host program can do the equivalent to this Lua code:

```lua
a = f("how", t.x, 14)
```

Here it is in C:

```lua
lua_getglobal(L, "f");                  /* function to be called */
lua_pushliteral(L, "how");                       /* 1st argument */
lua_getglobal(L, "t");                    /* table to be indexed */
lua_getfield(L, -1, "x");        /* push result of t.x (2nd arg) */
lua_remove(L, -2);                  /* remove 't' from the stack */
lua_pushinteger(L, 14);                          /* 3rd argument */
lua_call(L, 3, 1);     /* call 'f' with 3 arguments and 1 result */
lua_setglobal(L, "a");                         /* set global 'a' */
```

Note that the code above is *balanced*: at its end, the stack is back to its original configuration. This is considered good programming practice.