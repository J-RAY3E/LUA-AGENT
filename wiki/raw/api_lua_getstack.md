# lua_getstack

**Category**: API

### `lua_getstack`[-0, +0, –]

```lua
int lua_getstack (lua_State *L, int level, lua_Debug *ar);
```

Gets information about the interpreter runtime stack.

This function fills parts of a [`lua_Debug`](#lua_Debug) structure with an identification of the *activation record* of the function executing at a given level. Level 0 is the current running function, whereas level *n+1* is the function that has called level *n* (except for tail calls, which do not count in the stack). When called with a level greater than the stack depth, [`lua_getstack`](#lua_getstack) returns 0; otherwise it returns 1.