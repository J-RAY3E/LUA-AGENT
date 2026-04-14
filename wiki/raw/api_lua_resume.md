# lua_resume

**Category**: API

### `lua_resume`[-?, +?, –]

```lua
int lua_resume (lua_State *L, lua_State *from, int nargs,
                          int *nresults);
```

Starts and resumes a coroutine in the given thread `L`.

To start a coroutine, you push the main function plus any arguments onto the empty stack of the thread. then you call [`lua_resume`](#lua_resume), with `nargs` being the number of arguments. The function returns when the coroutine suspends, finishes its execution, or raises an unprotected error. When it returns without errors, `*nresults` is updated and the top of the stack contains the `*nresults` values passed to [`lua_yield`](#lua_yield) or returned by the body function. [`lua_resume`](#lua_resume) returns [`LUA_YIELD`](#pdf-LUA_YIELD) if the coroutine yields, [`LUA_OK`](#pdf-LUA_OK) if the coroutine finishes its execution without errors, or an error code in case of errors (see [§4.4.1](#4.4.1)). In case of errors, the error object is pushed on the top of the stack. (In that case, `nresults` is not updated, as its value would have to be 1 for the sole error object.)

To resume a suspended coroutine, you remove the `*nresults` yielded values from its stack, push the values to be passed as results from `yield`, and then call [`lua_resume`](#lua_resume).

The parameter `from` represents the coroutine that is resuming `L`. If there is no such coroutine, this parameter can be `NULL`.