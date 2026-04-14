# lua_getlocal

**Category**: API

### `lua_getlocal`[-0, +(0|1), –]

```lua
const char *lua_getlocal (lua_State *L, const lua_Debug *ar, int n);
```

Gets information about a local variable or a temporary value of a given activation record or a given function.

In the first case, the parameter `ar` must be a valid activation record that was filled by a previous call to [`lua_getstack`](#lua_getstack) or given as argument to a hook (see [`lua_Hook`](#lua_Hook)). The index `n` selects which local variable to inspect; see [`debug.getlocal`](#pdf-debug.getlocal) for details about variable indices and names.

[`lua_getlocal`](#lua_getlocal) pushes the variable's value onto the stack and returns its name.

In the second case, `ar` must be `NULL` and the function to be inspected must be on the top of the stack. In this case, only parameters of Lua functions are visible (as there is no information about what variables are active) and no values are pushed onto the stack.

Returns `NULL` (and pushes nothing) when the index is greater than the number of active local variables.