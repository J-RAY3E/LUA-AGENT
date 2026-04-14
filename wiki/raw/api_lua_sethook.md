# lua_sethook

**Category**: API

### `lua_sethook`[-0, +0, –]

```lua
void lua_sethook (lua_State *L, lua_Hook f, int mask, int count);
```

Sets the debugging hook function.

Argument `f` is the hook function. `mask` specifies on which events the hook will be called: it is formed by a bitwise OR of the constants `LUA_MASKCALL`, `LUA_MASKRET`, `LUA_MASKLINE`, and `LUA_MASKCOUNT`. The `count` argument is only meaningful when the mask includes `LUA_MASKCOUNT`. For each event, the hook is called as explained below:

* **The call hook**: is called when the interpreter calls a function. The hook is called just after Lua enters the new function.
* **The return hook**: is called when the interpreter returns from a function. The hook is called just before Lua leaves the function.
* **The line hook**: is called when the interpreter is about to start the execution of a new line of code, or when it jumps back in the code (even to the same line). This event only happens while Lua is executing a Lua function.
* **The count hook**: is called after the interpreter executes every `count` instructions. This event only happens while Lua is executing a Lua function.

Hooks are disabled by setting `mask` to zero.