# lua_closethread

**Category**: API

### `lua_closethread`[-0, +?, –]

```lua
int lua_closethread (lua_State *L, lua_State *from);
```

Resets a thread, cleaning its call stack and closing all pending to-be-closed variables. The parameter `from` represents the coroutine that is resetting `L`. If there is no such coroutine, this parameter can be `NULL`.

Unless `L` is equal to `from`, the call returns a status code: [`LUA_OK`](#pdf-LUA_OK) for no errors in the thread (either the original error that stopped the thread or errors in closing methods), or an error status otherwise. In case of error, the error object is put on the top of the stack.

If `L` is equal to `from`, it corresponds to a thread closing itself. In that case, the call does not return; instead, the resume that (re)started the thread returns. The thread must be running inside a resume.