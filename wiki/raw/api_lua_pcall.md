# lua_pcall

**Category**: API

### `lua_pcall`[-(nargs + 1), +(nresults|1), –]

```lua
int lua_pcall (lua_State *L, int nargs, int nresults, int msgh);
```

Calls a function (or a callable object) in protected mode.

Both `nargs` and `nresults` have the same meaning as in [`lua_call`](#lua_call). If there are no errors during the call, [`lua_pcall`](#lua_pcall) behaves exactly like [`lua_call`](#lua_call). However, if there is any error, [`lua_pcall`](#lua_pcall) catches it, pushes a single value on the stack (the error object), and returns an error code. Like [`lua_call`](#lua_call), [`lua_pcall`](#lua_pcall) always removes the function and its arguments from the stack.

If `msgh` is 0, then the error object returned on the stack is exactly the original error object. Otherwise, `msgh` is the stack index of a *message handler*. (This index cannot be a pseudo-index.) In case of runtime errors, this handler will be called with the error object and its return value will be the object returned on the stack by [`lua_pcall`](#lua_pcall).

Typically, the message handler is used to add more debug information to the error object, such as a stack traceback. Such information cannot be gathered after the return of [`lua_pcall`](#lua_pcall), since by then the stack has unwound.

The [`lua_pcall`](#lua_pcall) function returns one of the following status codes: [`LUA_OK`](#pdf-LUA_OK), [`LUA_ERRRUN`](#pdf-LUA_ERRRUN), [`LUA_ERRMEM`](#pdf-LUA_ERRMEM), or [`LUA_ERRERR`](#pdf-LUA_ERRERR).