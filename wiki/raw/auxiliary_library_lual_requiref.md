# luaL_requiref

**Category**: Auxiliary Library

### `luaL_requiref`[-0, +1, *e*]

```lua
void luaL_requiref (lua_State *L, const char *modname,
                    lua_CFunction openf, int glb);
```

If `package.loaded[modname]` is not true, calls the function `openf` with the string `modname` as an argument and sets the call result to `package.loaded[modname]`, as if that function has been called through [`require`](#pdf-require).

If `glb` is true, also stores the module into the global variable `modname`.

Leaves a copy of the module on the stack.